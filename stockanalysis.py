# -*- coding: utf-8 -*-


!pip install yfinance pandas numpy matplotlib seaborn plotly

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

def calculate_moving_averages(data: pd.DataFrame) -> pd.DataFrame:
    data["SMA20"] = data["Close"].rolling(window=20).mean()
    data["SMA50"] = data["Close"].rolling(window=50).mean()
    return data

def calculate_volatility(data: pd.DataFrame) -> pd.DataFrame:
    data["Volatility"] = data["Daily Return"].rolling(window=20).std()
    return data

def calculate_rsi(data: pd.DataFrame) -> pd.DataFrame:
    close = data["Close"]
    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    # SMA RSI
    roll_up = gain.rolling(14).mean()
    roll_down = loss.rolling(14).mean()
    RS = roll_up / roll_down
    data["RSI"] = 100 - (100 / (1 + RS))

    # EMA RSI
    roll_up_ema = gain.ewm(span=14, adjust=False).mean()
    roll_down_ema = loss.ewm(span=14, adjust=False).mean()
    RS_ema = roll_up_ema / roll_down_ema
    data["RSI_EMA"] = 100 - (100 / (1 + RS_ema))

    return data

def fetch_data(ticker="INFY.NS", period="1y"):
    data = yf.download(ticker, period=period)
    data = data.ffill()
    data.index = pd.to_datetime(data.index)
    data["Daily Return"] = data["Close"].pct_change()
    return data

ticker = "INFY.NS"   # You can change this (e.g., "AAPL", "TSLA", "RELIANCE.NS")
period = "1y"

data = fetch_data(ticker, period)
data = calculate_moving_averages(data)
data = calculate_volatility(data)
data = calculate_rsi(data)

data.head()

plt.figure(figsize=(12,6))
plt.plot(data.index, data["Close"], label="Close", color="blue")
plt.plot(data.index, data["SMA20"], label="20-Day SMA", color="orange")
plt.plot(data.index, data["SMA50"], label="50-Day SMA", color="red")
plt.title(f"{ticker} Stock with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(data["Daily Return"].dropna(), bins=50, kde=True, color="purple")
plt.title(f"{ticker} - Daily Returns Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(12,6))
plt.plot(data.index, data["RSI"], label="RSI (SMA)", color="purple")
plt.plot(data.index, data["RSI_EMA"], label="RSI (EMA)", color="blue")
plt.axhline(70, linestyle="--", color="red", alpha=0.7)
plt.axhline(30, linestyle="--", color="green", alpha=0.7)
plt.title(f"{ticker} - RSI (Relative Strength Index)")
plt.legend()
plt.show()
