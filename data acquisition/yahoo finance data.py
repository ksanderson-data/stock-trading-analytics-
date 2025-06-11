import yfinance as yf
import pandas as pd

# Pull 5 years of daily SPY index data
spy_data = yf.download("SPY", period="5y", interval="1d")
spy_data.to_csv("spy_5y.csv")
