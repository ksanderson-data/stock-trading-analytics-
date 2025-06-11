from pytrends.request import TrendReq

pytrends = TrendReq()
pytrends.build_payload(["SPY"], timeframe='today 5-y')
data = pytrends.interest_over_time()
data.to_csv("social_trends_spy.csv")