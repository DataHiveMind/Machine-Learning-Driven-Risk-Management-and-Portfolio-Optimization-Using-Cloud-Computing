import pandas as pd
import numpy as np
import joblib
import pyodbc
from azureml.core import Workspace, Model, Dataset
from azure.storage.blob import BlobServiceClient
from models import train_portfolio_nn, random_forest_predict
from data import fetch_market_data, save_to_sql
from feature_engineering import compute_moving_avg, compute_volatility
from risk_assessment import compute_sharpe_ratio, compute_value_at_risk
from trade_logging import track_trade

# Azure Blob Storage connection setup
AZURE_BLOB_CONNECTION_STRING = "your_azure_blob_connection_string"
CONTAINER_NAME = "financial-data"

def load_blob_data(blob_name):
    """Fetch financial dataset from Azure Blob Storage."""
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    
    blob_data = blob_client.download_blob().readall()
    df = pd.read_csv(pd.compat.StringIO(blob_data.decode('utf-8')))
    return df

# Setup Azure ML Workspace
ws = Workspace.from_config()

# Load financial data from Azure Blob
print("Fetching financial data from Azure Blob Storage...")
df = load_blob_data("market_data.csv")

# Process data
print("Performing feature engineering...")
df = compute_moving_avg(df)
df = compute_volatility(df)

# Check if new market data requires re-training
latest_data = df.iloc[-1]  # Latest market snapshot
if latest_data["volatility"] > 0.02:  # Example threshold
    print("Market conditions changed! Re-training model...")
    
    # Train Machine Learning Model
    features = ["volatility", "SMA_50", "momentum", "interest_rate"]
    target = ["portfolio_allocation_AAPL", "portfolio_allocation_MSFT"]
    X = df[features]
    y = df[target]
    
    rf_model = random_forest_predict(X, y, X)  # Train new model
    joblib.dump(rf_model, "models/random_forest_portfolio.pkl")

    # Deploy updated model in Azure ML
    print("Deploying updated model to Azure ML...")
    Model.register(workspace=ws, model_path="models/random_forest_portfolio.pkl", model_name="PortfolioOptimizer")

# Execute trade logging based on predictions
print("Logging trade executions...")
track_trade("2025-04-08", "AAPL", "BUY", 10, df["close_price"].iloc[-1])

# Perform risk assessment
print("Calculating Sharpe Ratio & VaR...")
sharpe_ratio = compute_sharpe_ratio(df["daily_returns"])
VaR_95 = compute_value_at_risk(df["daily_returns"], confidence_level=0.95)

print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Value at Risk (95% confidence): {VaR_95:.2f}")

print("Process completed successfully!")
