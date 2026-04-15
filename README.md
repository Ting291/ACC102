# Financial Ratio Analysis: PetroChina vs Sinopec

## 1. Problem & User 
This project compares the financial performance of China’s two largest oil companies – **PetroChina (601857)** and **Sinopec (600028)** – using key profitability and leverage ratios. The target users are **accounting students, equity analysts, or investors** who need a quick, data‑driven comparison of these two firms.

## 2. Data
- **Source**: WRDS (Wharton Research Data Services) – CSMAR Financial Master table  
- **Access date**: 15 April 2026  
- **Key fields**: `stkcd` (stock code), `accper` (reporting date), net profit, total assets, total equity, total revenue  
- **Time period**: 2021–2024 (year‑end December only)  

## 3. Methods
- **Data extraction**: SQL query inside Python to download raw data from WRDS  
- **Ratio calculation** (done in SQL):  
  - ROE = Net Profit / Total Equity  
  - ROA = Net Profit / Total Assets  
  - Profit Margin = Net Profit / Total Revenue  
  - Asset Turnover = Total Revenue / Total Assets  
  - Leverage = Total Assets / Total Equity  
- **Filtering**: keep only December year‑end reports, data from start_year (2021) onward  
- **Reshaping**: create pivot tables (companies as rows, years as columns)  
- **Formatting**: percentages for profitability ratios, raw ratios for leverage  

## 4. Key Findings
- **PetroChina** shows stronger and improving profitability (ROE 8.1% → 10.7%, Profit Margin 4.4% → 6.3%)  
- **Sinopec** has declining ROE (9.3% → 5.9%) and lower profit margins (~2%)  
- **Sinopec** operates with higher leverage (~2.1×) than PetroChina (~1.7×), implying more debt reliance  
- Both companies have similar asset turnover (~1.0–1.7×), but Sinopec’s efficiency is slightly higher  

## 5. How to run
1. Install required packages: `pip install wrds pandas`  
2. Replace `username = 'your_username'` with your WRDS credentials  
3. Run the notebook `ACC102.ipynb` top to bottom  
4. The notebook automatically:  
   - Connects to WRDS  
   - Downloads and calculates ratios  
   - Displays pivot tables and saves `financial_ratios.csv`  

## 6. Product link / Demo
- **GitHub repository**: [Add your repo URL here]  
- **Demo video**: [Add YouTube/Bilibili link here]  
- **Interactive version **: [https://acc102-h6xxngn4nevs8uwdr2fefg.streamlit.app/]  

## 7. Limitations & next steps
- Only two companies – can be extended to more oil & gas peers  
- Data stops at 2024 – update when 2025 reports become available  
- No visualisations yet – next step: add line charts of ROE / margin trends  
- Requires WRDS access – future version could cache data to reduce repeated downloads  
