# 📈 Quantitative Finance Portfolio Optimization 🚀  
### Cloud-Powered Machine Learning for Portfolio Strategy & Risk Management  

## **🔍 Project Overview**
This project leverages **machine learning, reinforcement learning, SQL-based trade logging, and Azure cloud computing** to dynamically optimize stock portfolio allocations based on market conditions.  

Through **automated data ingestion, real-time risk assessment, and scheduled model re-training**, it provides a cutting-edge solution for **adaptive financial decision-making**.

---

## **📊 Key Features & Updates**
✅ **Azure ML Integration:** Deploys machine learning portfolio models in the cloud.  
✅ **Automated Model Re-Training:** Reacts to volatility changes, ensuring optimal predictions.  
✅ **Cloud-Based Data Ingestion:** Fetches real-time market & macroeconomic data from **Azure Blob Storage**.  
✅ **SQL-Based Trade Logging:** Logs executed trades for historical tracking & compliance.  
✅ **Scheduled Updates via Azure Functions:** Runs **daily at 4PM EST** after market close.  
✅ **Risk Metrics (Sharpe Ratio, VaR):** Tracks portfolio performance with statistical insights.  
✅ **Power BI Real-Time Monitoring:** **Live portfolio dashboards** visualize trading decisions dynamically.  

---

## **🛠 Technologies Used**
| **Tech**           | **Purpose**                                           |
|--------------------|-------------------------------------------------------|
| **Python**        | Data processing, machine learning models (TensorFlow, PyTorch) |
| **R**             | Statistical risk analysis & financial modeling (quantmod, PerformanceAnalytics) |
| **SQL (Azure SQL)** | Storing market data, trade execution logs, and portfolio tracking |
| **Azure ML**      | Cloud deployment of ML models & automatic retraining |
| **Azure Blob Storage** | Scalable financial data ingestion for portfolio models |
| **Azure Functions** | Scheduled model updates **daily at 4PM EST** |
| **Power BI**      | Real-time **portfolio monitoring dashboards** |

---

## **📂 Directory Structure**
Quant-Finance-Portfolio-Optimization/ 
│── data/ # Raw & Processed Financial Data (from Azure Blob) 
│── models/ # ML & RL models for asset allocation 
│── sql/ # SQL queries for trade logging & risk analysis 
│── scripts/ # Training, backtesting, automated trade execution 
│── notebooks/ # Jupyter & R notebooks for modeling & analytics 
│── azure/ # Cloud deployment scripts (Azure ML, Azure Functions) 
│── requirements.txt # Dependencies │── README.md # Documentation 
│── main.py # Entry point for execution (automation & monitoring)

7️⃣ Monitor Portfolio in Power BI
Open Power BI → Connect to Azure SQL Database.

Select tables: trade_log, market_data, portfolio_allocation.

Build real-time dashboards to visualize financial trends.

🔄 Automated Scheduled Execution
💡 Azure Functions automatically update models daily at 4PM EST after market close. ✅ Fetches new market data. ✅ Checks portfolio performance. ✅ Retrains models if volatility shifts. ✅ Deploys updated models in Azure ML.

👨‍💻 Contributors & Future Enhancements
💡 Future Ideas: 🔥 Portfolio Rebalancing Automation (Dynamic trade execution). 🔥 Deep Reinforcement Learning (Optimized risk-adjusted strategies). 🔥 AI-driven Macro-Economic Forecasting (Predict inflation & interest rate trends).