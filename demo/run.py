# Find 50 top company symbols 

# Optimize and get report 
from empyrial import empyrial
from empyrial import get_report, Engine
PORTFOLIO = ["BABA", "PDD", "KO", "AMD","^IXIC"]
portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = PORTFOLIO,
      optimizer = "EF",
      min_weights = 0.01, #invest at least 5% of the capital in every assets
      max_weights = 0.5, #don't invest more than 35% in one asset
      rebalance = '1y',
      risk_manager = {"Stop Loss" : -0.2, "Take Profit" : 0.4}
)
get_report(portfolio)
empyrial(portfolio)
empyrial.orderbook.to_csv('orderbook.csv')

from the_oracle import oracle
  
oracle(
      portfolio=PORTFOLIO, #stocks you want to predict
      start_date = "2018-01-01", #date from which it will take data to predict
      weights = portfolio.weights, #allocate 30% to TSLA and 20% to AAPL...(equal weighting  by default)
      prediction_days=30 #number of days you want to predict
)

