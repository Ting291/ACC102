# Financial Ratio Comparison Tool | PetroChina vs Sinopec

Track 4 – Interactive Data Analysis Tool (Streamlit)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://acc102-h6xxngn4nevs8uwdr2fefg.streamlit.app/)

---

## 1. Problem & User

This interactive tool allows users to **compare financial ratios** (ROE, ROA, Profit Margin, Turnover, Leverage) between **PetroChina (601857)** and **Sinopec (600028)** from 2021 to 2024. The target users are **accounting students**, **equity analysts**, and **investors** who want an on‑demand, visual comparison without writing code or navigating complex databases.

---

## 2. Data

- **Source**: WRDS (Wharton Research Data Services) – CSMAR Financial Master table
- **Access date**: [15 April 2026]
- **Time period**: 2021–2024 (year‑end December only)
- **Key fields**: `stkcd`, `accper`, net profit, total assets, total equity, total revenue
- **Data file in repo**: `financial_ratios.csv` (cached so the app works without WRDS credentials)

---

## 3. Methods & Technical Implementation

### Backend (Python)

- **Data extraction**: SQL query from WRDS (see `ACC102.ipynb` for the original extraction)
- **Ratio calculations**:
  - **ROE** = Net Profit / Total Equity
  - **ROA** = Net Profit / Total Assets
  - **Profit Margin** = Net Profit / Total Revenue
  - **Asset Turnover** = Total Revenue / Total Assets
  - **Leverage** = Total Assets / Total Equity
- **Data cleaning**: keep only December year‑end reports, filter from 2021 onward

### Frontend (Streamlit)

- **Interactive widgets**: dropdown selector for company, slider for year range
- **Visualisations**: line charts showing trends over time
- **Comparison mode**: toggle to show both companies on the same chart
- **Data table**: raw numbers in a sortable/filterable table

### Deployment

- **Platform**: Streamlit Community Cloud (free)
- **Link**: https://acc102-h6xxngn4nevs8uwdr2fefg.streamlit.app/
- **Auto‑deploys**: from this GitHub repository on every `git push`

---

## 4. Key Findings

When you use the tool, you will observe:

- **PetroChina** shows improving profitability: **ROE** from 8.1% (2021) → 10.7% (2024), **Profit Margin** from 4.4% → 6.3%
- **Sinopec** has declining performance: **ROE** from 9.3% → 5.9%, **Profit Margin** stuck around 2%
- **Leverage** is consistently higher for **Sinopec** (~2.1×) than **PetroChina** (~1.7×), suggesting greater debt reliance
- **Asset Turnover** is similar for both (1.0–1.7×), typical for capital‑intensive oil & gas operations

---

## 5. How to Run Locally 

 1. Clone the repository
git clone https://github.com/Ting291/ACC102
cd acc102-financial-ratios

 2. Install dependencies
pip install -r requirements.txt

 3. Run the Streamlit app
streamlit run app.py

 requirements.txt:
 streamlit>=1.28.0
 pandas>=2.0.0
 plotly>=5.0.0

---

## 6. Product Links

| Type | Link |
|------|------|
| Live Interactive Tool | https://acc102-h6xxngn4nevs8uwdr2fefg.streamlit.app/ |
| Demo Video | [请修改：YouTube/Bilibili链接] |
| GitHub Repository | https://github.com/Ting291/ACC102|
| Jupyter Notebook | ACC102.ipynb |

---

## 7. Repository Structure

 ACC102/
 ── ACC102.ipynb           # Original data extraction & ratio calculation
 ── README.md              # This file
 ── app.py                 # Streamlit main application
 ── financial_ratios.csv   # Cleaned data (cached)
 ── requirements.txt       # Python dependencies

---

## 8. Limitations & Next Steps

 Current limitations:
 - Only two companies – could be extended to more oil & gas peers
 - Data ends at 2024 – update when 2025 reports become available
 - No user-uploaded data functionality
 - Free tier Streamlit Cloud may sleep after inactivity

 Next steps:
 - Add benchmark comparison (industry average)
 - Include financial health score
 - Add PDF report export
 - Implement real-time data refresh

---

## 9. Acknowledgements

 Data provided by WRDS (Wharton Research Data Services) – CSMAR database
 Built with Streamlit, Pandas, and Plotly
