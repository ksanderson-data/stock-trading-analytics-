import yfinance as yf
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp500_df = pd.read_html(url, header=0)[0]
sp500_df.to_csv("sp500_companies.csv", index=False)
