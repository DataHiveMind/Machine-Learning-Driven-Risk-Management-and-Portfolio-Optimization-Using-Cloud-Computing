import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("data/financial_data.csv")

# Feature selection
features = ["volatility", "SMA_50", "momentum", "interest_rate"]
target = ["portfolio_allocation_AAPL", "portfolio_allocation_MSFT"]

X = df[features]
y = df[target]

# Preprocess data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model
import joblib
joblib.dump(model, "models/random_forest_portfolio.pkl")
print("Model saved successfully!")
