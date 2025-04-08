import logging
import pandas as pd
import joblib
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from azureml.core import Workspace, Model
from models import random_forest_predict
from feature_engineering import compute_moving_avg, compute_volatility

# Azure Configurations
AZURE_BLOB_CONNECTION_STRING = "your_azure_blob_connection_string"
CONTAINER_NAME = "financial-data"

# Load Azure ML Workspace
ws = Workspace.from_config()

def load_blob_data(blob_name):
    """Fetch financial dataset from Azure Blob Storage."""
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    
    blob_data = blob_client.download_blob().readall()
    df = pd.read_csv(pd.compat.StringIO(blob_data.decode('utf-8')))
    return df

def retrain_model():
    """Retrains ML model based on updated market data."""
    logging.info("Fetching latest market data...")
    df = load_blob_data("market_data.csv")

    # Feature Engineering
    df = compute_moving_avg(df)
    df = compute_volatility(df)

    features = ["volatility", "SMA_50", "momentum", "interest_rate"]
    target = ["portfolio_allocation_AAPL", "portfolio_allocation_MSFT"]
    
    X = df[features]
    y = df[target]

    # Train New Model
    logging.info("Retraining portfolio optimization model...")
    model = random_forest_predict(X, y, X)

    # Save and Deploy Model
    joblib.dump(model, "models/random_forest_portfolio.pkl")
    Model.register(workspace=ws, model_path="models/random_forest_portfolio.pkl", model_name="PortfolioOptimizer")
    
    logging.info("Model updated and deployed successfully!")

# Azure Timer Function Trigger
def main(timer: func.TimerRequest) -> None:
    logging.info("Azure Function Triggered: Daily Model Update at 4PM EST")
    
    try:
        retrain_model()

        logging.info("Portfolio model re-trained and updated!")
        return func.HttpResponse("Model re-trained successfully!", status_code=200)
    except Exception as e:
        logging.error(f"Error during model retraining: {e}")
        return func.HttpResponse("Error during model retraining.", status_code=500)