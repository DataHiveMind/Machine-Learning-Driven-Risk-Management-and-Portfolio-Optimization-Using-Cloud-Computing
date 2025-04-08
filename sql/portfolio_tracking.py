import pyodbc
import pandas as pd

# Azure SQL Database Connection
SQL_SERVER = "your-sql-server.database.windows.net"
DATABASE = "your-database"
USERNAME = "your-username"
PASSWORD = "your-password"
DRIVER = "{ODBC Driver 17 for SQL Server}"

def track_portfolio(trades):
    """Store trade execution logs in Azure SQL Database."""
    conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SQL_SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}')
    cursor = conn.cursor()

    for trade in trades:
        cursor.execute("""
        INSERT INTO portfolio_log (date, asset, action, quantity, price)
        VALUES (?, ?, ?, ?, ?)
        """, trade["date"], trade["asset"], trade["action"], trade["quantity"], trade["price"])

    conn.commit()
    conn.close()
    print("Portfolio trades stored successfully!")

def fetch_trade_history():
    """Retrieve historical trade execution data."""
    conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SQL_SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}')
    query = "SELECT * FROM portfolio_log ORDER BY date DESC"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Example Usage
if __name__ == "__main__":
    trades = [
        {"date": "2025-04-08", "asset": "AAPL", "action": "BUY", "quantity": 10, "price": 165.2},
        {"date": "2025-04-08", "asset": "TSLA", "action": "SELL", "quantity": 5, "price": 225.5}
    ]
    track_portfolio(trades)
    print(fetch_trade_history())
