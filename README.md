Stock Trading Analytics — SPY Trend Prediction & Simulation

Author: Kyle Sanderson

Tools: python · pandas · scikit-learn · Power BI

This project applies trend forecasting and portfolio simulation to the SPY ETF (S&P 500 index fund) using historical market data. It demonstrates how time series analysis, feature engineering, and classification models can be used to evaluate trading strategies.

Feature Engineering

Rolling Volatility (21-day std)
	•	Moving Averages (10D, 50D, 200D)
	•	ATR (Average True Range)`
	•	Momentum: RSI, MACD, MACD Signal
	•	Rolling Sharpe Ratio
	•	Lagged Returns (t-1, t-2, t-3)

Modeling
	•	Model 1: Logistic Regression — interpretable baseline
	•	Model 2: Random Forest Classifier — handles non-linear relationships
	•	Evaluation
	•	Accuracy
	•	Precision, Recall, F1
	•	Strategy vs. SPY returns

Power BI Dashboard
Power BI showcases predicted vs actual trends, strategy return vs SPY, and KPI metrics.
