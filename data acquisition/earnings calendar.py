import finnhub

finnhub_client = finnhub.Client(api_key="d0u5r89r01qn5fk3bm90d0u5r89r01qn5fk3bm9g")
earnings = finnhub_client.earnings_calendar()
# Export to CSV manually if data is nested
