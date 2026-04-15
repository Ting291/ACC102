import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="PetroChina vs Sinopec Financial Ratios", layout="wide")
st.title("🛢️ PetroChina vs Sinopec Financial Ratio")
st.markdown("### ROE、ROA、Net Profit Margin、Total Asset Turnover、Leverage Ratio")

@st.cache_data
def load_data():
    try:
        with open("financial_ratios.csv", 'r', encoding='utf-8-sig') as f:
            content = f.read()
    except FileNotFoundError:
        st.error("❌ financial_ratios.csv not found，请Please ensure the file is uploaded to GitHub。")
        st.stop()
    
    lines = content.strip().split('\n')
    cleaned_lines = [line.strip('"') for line in lines]
    cleaned_content = '\n'.join(cleaned_lines)
    
    df = pd.read_csv(io.StringIO(cleaned_content))
    df["year"] = df["year"].astype(int)
    df["Company"] = df["Company"].str.strip()
    return df

df = load_data()

# define metrics
metrics = {
    "roe": "ROE (Return on Equity %)",
    "roa": "ROA (Return on Assets %)",
    "profitmargin": "Net Profit Margin %",
    "turnover": "Total Asset Turnover %",
    "leverage": "Leverage Ratio (no %)"
}

selected_metric = st.sidebar.selectbox(
    "Select a financial metric to compare",
    options=list(metrics.keys()),
    format_func=lambda x: metrics[x]
)

years = sorted(df["year"].unique())
year_range = st.sidebar.slider(
    "Select year range",
    min_value=int(min(years)),
    max_value=int(max(years)),
    value=(int(min(years)), int(max(years)))
)

filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

if filtered_df.empty:
    st.warning("⚠️ No data available for the selected year range")
    st.stop()

# KPI
latest_year = filtered_df["year"].max()
latest_data = filtered_df[filtered_df["year"] == latest_year]

col1, col2 = st.columns(2)
with col1:
    petrochina_roe = latest_data[latest_data["Company"]=="PetrolChina"]["roe"].values[0] * 100
    st.metric("⛽ PetrolChina ROE", f"{petrochina_roe:.1f}%")
with col2:
    sinopec_roe = latest_data[latest_data["Company"]=="Sinopec"]["roe"].values[0] * 100
    st.metric("🏭 Sinopec ROE", f"{sinopec_roe:.1f}%")

# Line Chart
st.subheader(f"📈 Trend of {metrics[selected_metric]} ")
plot_df = filtered_df.copy()
if selected_metric != "leverage":
    plot_df[selected_metric] = plot_df[selected_metric] * 100

fig_line = px.line(
    plot_df,
    x="year",
    y=selected_metric,
    color="Company",
    markers=True,
    title=f"{metrics[selected_metric]} Over Time",
    labels={selected_metric: metrics[selected_metric], "year": "Year"}
)
st.plotly_chart(fig_line, use_container_width=True)

# Bar Chart
st.subheader(f"📊 Annual Comparison of {metrics[selected_metric]} ")
fig_bar = px.bar(
    plot_df,
    x="year",
    y=selected_metric,
    color="Company",
    barmode="group",
    title=f"Annual Coparison of {metrics[selected_metric]}",
    labels={selected_metric: metrics[selected_metric], "year": "Year"}
)
st.plotly_chart(fig_bar, use_container_width=True)

with st.expander("📋 View Raw Data"):
    st.dataframe(filtered_df)

st.subheader("💡 Key Insights")
st.markdown("""
- **PetroChina ROE consistently higher than Sinopec**: 2024 PetroChina 10.7% vs Sinopec 5.9%
- **Net Profit Margin**: PetroChina rose from 4.4% to 6.3%; Sinopec fell from 3.1% to 1.9%
- **Total Asset Turnover**: Both > 1; Sinopec higher (≈1.5–1.7), PetroChina ≈1.0–1.2
- **Leverage Ratio**: Sinopec ≈2.1x, PetroChina ≈1.6–1.8x; Sinopec uses higher financial leverage
""")

st.caption("Data Source: CSMAR (via WRDS) | Period: 2021–2024")
