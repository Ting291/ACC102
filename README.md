# Financial Ratio Comparison Tool | PetroChina vs Sinopec

**Track 4 – Interactive Data Analysis Tool (Streamlit)**  

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://[请修改].streamlit.app)

---

```bash
\033[1;31m## 1. Problem & User\033[0m

This interactive tool allows users to compare financial ratios (ROE, ROA, Profit Margin, Turnover, Leverage) between PetroChina (601857) and Sinopec (600028) from 2021 to 2024. The target users are accounting students, equity analysts, and investors who want an on-demand, visual comparison without writing code or navigating complex databases.

\033[1;31m## 2. Data\033[0m

- Source: WRDS (Wharton Research Data Services) – CSMAR Financial Master table
- Access date: [请修改，例如：15 April 2026]
- Time period: 2021–2024 (year-end December only)
- Key fields: stkcd, accper, net profit, total assets, total equity, total revenue
- Data file in repo: financial_ratios.csv (cached so the app works without WRDS credentials)

\033[1;31m## 3. Methods & Technical Implementation\033[0m

\033[1;31m### Backend (Python)\033[0m

- Data extraction: SQL query from WRDS (see ACC102.ipynb for the original extraction)
- Ratio calculations:
  - ROE = Net Profit / Total Equity
  - ROA = Net Profit / Total Assets
  - Profit Margin = Net Profit / Total Revenue
  - Asset Turnover = Total Revenue / Total Assets
  - Leverage = Total Assets / Total Equity
- Data cleaning: keep only December year-end reports, filter from 2021 onward

\033[1;31m### Frontend (Streamlit)\033[0m

- Interactive widgets: dropdown selector for company, slider for year range
- Visualisations: line charts showing trends over time
- Comparison mode: toggle to show both companies on the same chart
- Data table: raw numbers in a sortable/filterable table

\033[1;31m### Deployment\033[0m

- Platform: Streamlit Community Cloud (free)
- Link: https://[请修改].streamlit.app
- Auto-deploys: from this GitHub repository on every git push

\033[1;31m## 4. Key Findings\033[0m

When you use the tool, you will observe:

- PetroChina shows improving profitability: ROE from 8.1% (2021) -> 10.7% (2024), Profit Margin from 4.4% -> 6.3%
- Sinopec has declining performance: ROE from 9.3% -> 5.9%, Profit Margin stuck around 2%
- Leverage is consistently higher for Sinopec (~2.1x) than PetroChina (~1.7x), suggesting greater debt reliance
- Asset Turnover is similar for both (1.0–1.7x), typical for capital-intensive oil & gas operations

\033[1;31m## 5. How to Run Locally\033[0m

# 1. Clone the repository
git clone https://github.com/[请修改]/acc102-financial-ratios.git
cd acc102-financial-ratios

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py

# requirements.txt:
# streamlit>=1.28.0
# pandas>=2.0.0
# plotly>=5.0.0

The app will open in your browser at http://localhost:8501

\033[1;31m## 6. Product Links\033[0m

# Live Interactive Tool: https://[请修改].streamlit.app
# Demo Video: [请修改：YouTube/Bilibili链接]
# GitHub Repository: https://github.com/[请修改]/acc102-financial-ratios
# Jupyter Notebook: ACC102.ipynb

\033[1;31m## 7. Repository Structure\033[0m

# acc102-financial-ratios/
# ├── app.py                 # Streamlit main application
# ├── ACC102.ipynb           # Original data extraction & ratio calculation
# ├── financial_ratios.csv   # Cleaned data (cached)
# ├── requirements.txt       # Python dependencies
# ├── README.md              # This file
# └── figures/               # Charts and screenshots (optional)

\033[1;31m## 8. Limitations & Next Steps\033[0m

# Current limitations:
# - Only two companies – could be extended to more oil & gas peers
# - Data ends at 2024 – update when 2025 reports become available
# - No user-uploaded data functionality
# - Free tier Streamlit Cloud may sleep after inactivity

# Next steps:
# - Add benchmark comparison (industry average)
# - Include financial health score
# - Add PDF report export
# - Implement real-time data refresh

\033[1;31m## 9. Acknowledgements\033[0m

# Data provided by WRDS (Wharton Research Data Services) – CSMAR database
# Built with Streamlit, Pandas, and Plotly
