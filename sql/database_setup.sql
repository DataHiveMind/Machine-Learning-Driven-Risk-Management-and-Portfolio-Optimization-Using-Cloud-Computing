-- Create the market_data table (historical stock prices)
CREATE TABLE market_data (
    id INT PRIMARY KEY IDENTITY,
    date DATE NOT NULL,
    ticker VARCHAR(10) NOT NULL,
    open_price FLOAT NOT NULL,
    close_price FLOAT NOT NULL,
    high_price FLOAT NOT NULL,
    low_price FLOAT NOT NULL,
    volume INT NOT NULL
);

-- Create the macroeconomic_data table (interest rates, inflation, volatility index)
CREATE TABLE macroeconomic_data (
    id INT PRIMARY KEY IDENTITY,
    date DATE NOT NULL,
    interest_rate FLOAT NOT NULL,
    inflation_rate FLOAT NOT NULL,
    volatility_index FLOAT NOT NULL
);

-- Create the trade_log table (tracks portfolio trades)
CREATE TABLE trade_log (
    id INT PRIMARY KEY IDENTITY,
    date DATE NOT NULL,
    asset VARCHAR(10) NOT NULL,
    action VARCHAR(4) CHECK (action IN ('BUY', 'SELL')),
    quantity INT NOT NULL,
    price FLOAT NOT NULL
);

-- Create the portfolio_allocation table (stores recommended ML-driven allocations)
CREATE TABLE portfolio_allocation (
    id INT PRIMARY KEY IDENTITY,
    date DATE NOT NULL,
    asset VARCHAR(10) NOT NULL,
    recommended_weight FLOAT NOT NULL,
    model_type VARCHAR(50) NOT NULL
);

INSERT INTO market_data (date, ticker, open_price, close_price, high_price, low_price, volume)
VALUES ('2025-04-08', 'AAPL', 162.5, 165.2, 167.0, 160.8, 12000000);

INSERT INTO macroeconomic_data (date, interest_rate, inflation_rate, volatility_index)
VALUES ('2025-04-08', 3.5, 2.1, 18.4);

INSERT INTO trade_log (date, asset, action, quantity, price)
VALUES ('2025-04-08', 'TSLA', 'BUY', 15, 220.3);

SELECT asset, SUM(quantity) AS total_quantity, AVG(price) AS avg_price
FROM trade_log
GROUP BY asset;
