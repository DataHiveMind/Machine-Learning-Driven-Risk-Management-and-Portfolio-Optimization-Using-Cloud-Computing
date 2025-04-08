from azureml.core import Workspace, Model

ws = Workspace.from_config()
model = Model.register(workspace=ws, model_path="models/random_forest_portfolio.pkl", model_name="PortfolioOptimizer")

print("Machine learning model successfully deployed in Azure!")
