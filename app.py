import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PetroChina vs Sinopec 财务比率对比", layout="wide")
st.title("🛢️ 中国石油 vs 中国石化 财务比率对比")
st.markdown("### 基于 ROE、ROA、利润率、周转率、杠杆倍数")

@st.cache_data
def load_data():
    df = pd.read_csv("financial_ratios.csv")
    df["year"] = df["year"].astype(int)
    return df

df = load_data()

# 注意：你的 CSV 中 Company 列的值是 'PetrolChina ' (带空格) 和 'Sinopec'
# 为了显示美观，可以统一去掉空格
df["Company"] = df["Company"].str.strip()

metrics = {
    "roe": "ROE (净资产收益率 %)",
    "roa": "ROA (总资产收益率 %)",
    "profitmargin": "净利润率 %",
    "turnover": "总资产周转率 %",
    "leverage": "杠杆倍数 (无%)"
}

selected_metric = st.sidebar.selectbox(
    "选择要对比的财务指标",
    options=list(metrics.keys()),
    format_func=lambda x: metrics[x]
)

years = sorted(df["year"].unique())
year_range = st.sidebar.slider(
    "选择年份范围",
    min_value=min(years),
    max_value=max(years),
    value=(min(years), max(years))
)

filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# 最新一年的 KPI 卡片
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

# 原始数据
with st.expander("📋 查看原始数据"):
    st.dataframe(filtered_df)

# 分析结论（根据你 notebook 中的实际数据调整）
st.subheader("💡 核心发现")
st.markdown("""
- **中国石油的 ROE 持续高于中国石化**：2024 年石油 ROE 约 10.7%，石化约 5.9%
- **净利润率**：石油从 4.4% 升至 6.3%，石化从 3.1% 降至 1.9%，石油盈利能力更强且改善
- **总资产周转率**：两家均 >1，但石化更高（约 1.5-1.7），石油约 1.0-1.2
- **杠杆倍数**：石化约 2.1 倍，石油约 1.6-1.8 倍，石化财务杠杆更高
""")

st.caption("数据来源：CSMAR (via WRDS) | 分析期间：2021-2024")