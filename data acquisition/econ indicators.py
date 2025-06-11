from fredapi import Fred

fred = Fred(api_key='f8933dd12039b1b2eff009ecd59e10d4')
gdp = fred.get_series('GDP')  # Replace with any indicator
gdp.to_csv("economic_gdp.csv")
