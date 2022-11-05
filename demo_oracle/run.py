"""
pip install pystan==2.19.1.1
pip install prophet==1.0
pip install the-oracle

"""

from the_oracle import oracle
PORTFOLIO = ["BABA", "PDD", "KO", "AMD","^IXIC"]
WEIGHTS = [0.01, 0.01, 0.47, 0.5, 0.01]
oracle(
      portfolio=PORTFOLIO, #stocks you want to predict
      start_date = "2018-01-01", #date from which it will take data to predict
      weights = WEIGHTS, #allocate 30% to TSLA and 20% to AAPL...(equal weighting  by default)
      prediction_days=30 #number of days you want to predict
)

