import pyodbc
import pandas as pd

# Azure SQL Database Connection
SQL_SERVER = "your-sql-server.database.windows.net"
DATABASE = "your-database"
USERNAME = "your-username"
PASSWORD = "your-password"
DRIVER = "{ODBC Driver 17 for SQL Server}"

def track_trade(date, asset, action, quantity, price):
    """Store trade execution data in Azure SQL Database."""
    conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SQL_SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO trade_log (date, asset, action, quantity, price)
        VALUES (?, ?, ?, ?, ?)
    """, date, asset, action, quantity, price)

    conn.commit()
    conn.close()
    print("Trade execution stored successfully!")

# Example Usage
track_trade("2025-04-08", "AAPL", "BUY", 10, 165.2)
