import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class PortfolioOptimizerNN(nn.Module):
    """Neural network for portfolio optimization."""
    def __init__(self, input_dim):
        super(PortfolioOptimizerNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, input_dim)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))  # Asset allocation ratios
        return x

def train_portfolio_nn(X_train, y_train, input_dim, epochs=100, lr=0.001):
    """Train portfolio optimization neural network."""
    model = PortfolioOptimizerNN(input_dim)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()

    X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)

    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(X_train_tensor)
        loss = criterion(output, y_train_tensor)
        loss.backward()
        optimizer.step()
    
    return model

def random_forest_predict(X_train, y_train, X_test):
    """Train and predict using Random Forest for portfolio allocation."""
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Example Usage
if __name__ == "__main__":
    df = pd.read_csv("data/financial_data.csv")

    features = ["volatility", "SMA_50", "momentum", "interest_rate"]
    target = ["portfolio_allocation_AAPL", "portfolio_allocation_MSFT"]
    
    X = df[features]
    y = df[target]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(pd.DataFrame(X_scaled), y, test_size=0.2)

    # Train Neural Network Model
    nn_model = train_portfolio_nn(X_train, y_train, input_dim=len(features))

    # Train Random Forest Model
    rf_predictions = random_forest_predict(X_train, y_train, X_test)
    
    print("Portfolio Allocation Predictions:", rf_predictions)
