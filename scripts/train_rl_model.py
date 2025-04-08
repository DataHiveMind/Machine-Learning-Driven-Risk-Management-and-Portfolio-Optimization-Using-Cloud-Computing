from stable_baselines3 import PPO
import gym
import numpy as np
from stable_baselines3.common.envs import DummyVecEnv

class PortfolioTradingEnv(gym.Env):
    """Stock trading environment for RL portfolio optimization."""

    def __init__(self, stock_data):
        super(PortfolioTradingEnv, self).__init__()
        self.stock_data = stock_data
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(len(stock_data.columns),))
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(len(stock_data.columns),))

    def step(self, action):
        reward = np.random.rand()  # Placeholder for actual reward calculation
        done = False
        return self.stock_data.iloc[self.current_step].values, reward, done, {}

data = np.random.rand(1000, 10)
env = DummyVecEnv([lambda: PortfolioTradingEnv(pd.DataFrame(data))])

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Save RL model
model.save("models/ppo_portfolio_optimizer")
print("Reinforcement learning model trained & saved successfully!")
