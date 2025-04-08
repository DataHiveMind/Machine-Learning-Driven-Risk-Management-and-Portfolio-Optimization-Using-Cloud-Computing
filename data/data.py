import pandas as pd
import numpy as np
import pyodbc
import yfinance as yf
from azure.storage.blob import BlobServiceClient

# Azure SQL Database Connection
SQL_SERVER = "your-sql-server.database.windows.net"
DATABASE = "your-database"
USERNAME = "your-username"
PASSWORD = "your-password"
DRIVER = "{ODBC Driver 17 for SQL Server}"

def fetch_market_data(tickers, start_date, end_date):
    """Fetch stock price data from Yahoo Finance."""
    data = {ticker: yf.download(ticker, start=start_date, end=end_date) for ticker in tickers}
    return data

def save_to_sql(data):
    """Save stock data to Azure SQL Database."""
    conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SQL_SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}')
    cursor = conn.cursor()
    
    for ticker, df in data.items():
        for index, row in df.iterrows():
            cursor.execute("""
            INSERT INTO market_data (date, ticker, open_price, close_price, volume)
            VALUES (?, ?, ?, ?, ?)
            """, index, ticker, row['Open'], row['Close'], row['Volume'])
    
    conn.commit()
    conn.close()
    print("Data saved to Azure SQL Database.")

def save_to_azure_blob(data, container_name="financial-data"):
    """Store processed CSV files in Azure Blob Storage."""
    connect_str = "your_azure_blob_connection_string"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    for ticker, df in data.items():
        df.to_csv(f"{ticker}.csv")  # Save locally
        
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f"{ticker}.csv")
        with open(f"{ticker}.csv", "rb") as data_file:
            blob_client.upload_blob(data_file, overwrite=True)
    
    print("Data stored in Azure Blob Storage.")

# Example Usage
if __name__ == "__main__":
    tickers = ["AAPL", "GOOG", "MSFT"]
    data = fetch_market_data(tickers, "2020-01-01", "2025-01-01")
    
    save_to_sql(data)  # Store in Azure SQL
    save_to_azure_blob(data)  # Store in Azure Blob
