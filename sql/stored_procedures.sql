-- Stored Procedure: Insert a new trade execution
CREATE PROCEDURE log_trade
    @trade_date DATE,
    @asset VARCHAR(10),
    @action VARCHAR(4),
    @quantity INT,
    @price FLOAT
AS
BEGIN
    INSERT INTO trade_log (date, asset, action, quantity, price)
    VALUES (@trade_date, @asset, @action, @quantity, @price);
END
GO

-- Execute trade transaction
EXEC log_trade '2025-04-08', 'AAPL', 'BUY', 10, 165.2;
