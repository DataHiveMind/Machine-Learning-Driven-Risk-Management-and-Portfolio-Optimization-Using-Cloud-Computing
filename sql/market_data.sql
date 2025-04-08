SELECT date, stock_price, inflation_rate, interest_rate, volatility_index
FROM market_data
WHERE date BETWEEN '2015-01-01' AND '2025-01-01';

CREATE TABLE market_data (
    id INT PRIMARY KEY IDENTITY,
    date DATE,
    ticker VARCHAR(10),
    open_price FLOAT,
    close_price FLOAT,
    volume INT
);
