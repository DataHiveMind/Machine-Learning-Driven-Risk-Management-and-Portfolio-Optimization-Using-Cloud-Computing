import pandas as pd
import numpy as np

def compute_sharpe_ratio(returns, risk_free_rate=0.01):
    """Calculate Sharpe Ratio."""
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

df = pd.read_csv("data/financial_data.csv")
df["daily_returns"] = df["close_price"].pct_change()

sharpe_ratio = compute_sharpe_ratio(df["daily_returns"])
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
