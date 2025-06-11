from fredapi import Fred

fred = Fred(api_key='f8933dd12039b1b2eff009ecd59e10d4')

ffr = fred.get_series('FEDFUNDS')
ffr.to_csv("interest_rates.csv")
