SELECT 
    asset,
    AVG(daily_return) AS avg_return,
    STDEV(daily_return) AS std_dev,
    (AVG(daily_return) - 0.01) / STDEV(daily_return) AS sharpe_ratio -- Assuming 1% risk-free rate
FROM market_data
GROUP BY asset;

SELECT asset, 
    PERCENTILE_CONT(0.05) WITHIN GROUP (ORDER BY daily_return) AS VaR_95
FROM market_data
GROUP BY asset;
