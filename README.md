# 📊 Stock Analysis with Python (Infosys Example)

This project analyzes stock market data using **Yahoo Finance** and visualizes technical indicators such as:
- Moving Averages (SMA20, SMA50)
- Volatility
- RSI (SMA & EMA)

## 🚀 Features
- Works for any stock ticker (NSE/NYSE/NASDAQ)
- Plots Moving Averages with stock price
- Plots daily returns distribution
- Plots RSI with overbought/oversold zones
- Runs both as a **script** and a **Jupyter/Colab notebook**

---

## 📂 Repository Structure
- `stockanalysis.ipynb` → Colab-ready notebook (exploratory analysis with inline plots)
- `stockanalysis.py` → Script version (run from terminal)
- `utils/indicators.py` → Helper functions for calculations
- `requirements.txt` → Dependencies
- `plots/` → Example plots (optional, can include saved PNGs)

---

## 🛠️ Installation (Local)
```bash
git clone https://github.com/sourabh11001/technical-stock-analysis.git
cd stock-analysis
pip install -r requirements.txt

