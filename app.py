import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PetroChina vs Sinopec 财务比率对比", layout="wide")
st.title("🛢️ 中国石油 vs 中国石化 财务比率对比")
st.markdown("### ROE、ROA、净利润率、总资产周转率、杠杆倍数")

@st.cache_data
def load_data():
    # 检查文件是否存在
    import os
    if not os.path.exists("financial_ratios.csv"):
        st.error("❌ 错误：找不到 'financial_ratios.csv' 文件。请确保该文件与 app.py 在同一目录下，并已上传到 GitHub。")
        st.stop()
    
    df = pd.read_csv("financial_ratios.csv")
    
    # 打印列名（调试用，部署后可注释）
    st.write("调试信息：CSV 列名为", list(df.columns))
    
    # 检查是否有 'year' 列（大小写不敏感）
    if 'year' not in df.columns:
        # 尝试找大小写不同的列名
        possible_year = [col for col in df.columns if col.lower() == 'year']
        if possible_year:
            df.rename(columns={possible_year[0]: 'year'}, inplace=True)
        else:
            st.error("❌ CSV 文件中缺少 'year' 列，请检查导出的数据。")
            st.stop()
    
    # 转换 year 为整数，处理可能的非数字值
    try:
        df["year"] = pd.to_numeric(df["year"], errors='coerce').astype('Int64')
        # 删除 year 为空的行
        df = df.dropna(subset=['year']).copy()
    except Exception as e:
        st.error(f"❌ year 列转换失败：{e}")
        st.stop()
    
    # 确保 Company 列存在并清理空格
    if 'Company' not in df.columns:
        st.error("❌ CSV 文件中缺少 'Company' 列。")
        st.stop()
    df["Company"] = df["Company"].str.strip()
    
    return df

# 调用加载函数
df = load_data()

# 定义指标
metrics = {
    "roe": "ROE (净资产收益率 %)",
    "roa": "ROA (总资产收益率 %)",
    "profitmargin": "净利润率 %",
    "turnover": "总资产周转率 %",
    "leverage": "杠杆倍数 (无%)"
}

# 侧边栏
selected_metric = st.sidebar.selectbox(
    "选择要对比的财务指标",
    options=list(metrics.keys()),
    format_func=lambda x: metrics[x]
)

years = sorted(df["year"].unique())
year_range = st.sidebar.slider(
    "选择年份范围",
    min_value=int(min(years)),
    max_value=int(max(years)),
    value=(int(min(years)), int(max(years)))
)

filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

if filtered_df.empty:
    st.warning("⚠️ 没有数据符合所选年份范围，请调整范围。")
    st.stop()

# KPI 卡片
latest_year = filtered_df["year"].max()
latest_data = filtered_df[filtered_df["year"] == latest_year]

col1, col2 = st.columns(2)
with col1:
    petrochina_roe = latest_data[latest_data["Company"]=="PetrolChina"]["roe"].values[0] * 100
    st.metric("⛽ 中国石油 ROE", f"{petrochina_roe:.1f}%")
with col2:
    sinopec_roe = latest_data[latest_data["Company"]=="Sinopec"]["roe"].values[0] * 100
    st.metric("🏭 中国石化 ROE", f"{sinopec_roe:.1f}%")

# 折线图
st.subheader(f"📈 {metrics[selected_metric]} 趋势对比")
plot_df = filtered_df.copy()
if selected_metric != "leverage":
    plot_df[selected_metric] = plot_df[selected_metric] * 100

fig_line = px.line(
    plot_df,
    x="year",
    y=selected_metric,
    color="Company",
    markers=True,
    title=f"{metrics[selected_metric]} 随时间变化",
    labels={selected_metric: metrics[selected_metric], "year": "年份"}
)
st.plotly_chart(fig_line, use_container_width=True)

# 柱状图
st.subheader(f"📊 各年份 {metrics[selected_metric]} 对比")
fig_bar = px.bar(
    plot_df,
    x="year",
    y=selected_metric,
    color="Company",
    barmode="group",
    title=f"{metrics[selected_metric]} 年度对比",
    labels={selected_metric: metrics[selected_metric], "year": "年份"}
)
st.plotly_chart(fig_bar, use_container_width=True)

with st.expander("📋 查看原始数据"):
    st.dataframe(filtered_df)

st.subheader("💡 核心发现")
st.markdown("""
- **中国石油 ROE 持续高于中国石化**：2024 年石油 10.7% vs 石化 5.9%
- **净利润率**：石油从 4.4% 升至 6.3%，石化从 3.1% 降至 1.9%
- **总资产周转率**：两家均 >1，石化更高（约 1.5-1.7），石油约 1.0-1.2
- **杠杆倍数**：石化约 2.1 倍，石油约 1.6-1.8 倍，石化财务杠杆更高
""")

st.caption("数据来源：CSMAR (via WRDS) | 分析期间：2021-2024")
