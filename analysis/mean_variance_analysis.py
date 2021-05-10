# https://towardsdatascience.com/cryptocurrencies-the-new-frontier-part-1-940e787c7ab9
# https://towardsdatascience.com/cryptocurrencies-the-new-frontier-part-2-7218c6a489f9

# Measures in finance
## return: the % change in the stock price over a given ime interval
### - rate of return
### - logarithmic return

## rate of return vs. logarithmic return: https://chandlerfang.com/2017/01/09/arithmetic-vs-logarithmic-rates-of-return/

## volatility: standard deviation of the return

## expected return of the total portfolio is the weighted average of the expected returns of the individual stocks in the portfolio.

## expected variance of the portifolio is a product of the variance of the individual stocks, their respective weights in the overall portfolio and the correlation between each pair of stocks.

# Mean-Variance Analysis
## aka, Modern Portfolio Theory (MPT)
## Harry Markowitz, 1952
## main ideia: by tweaking the weights of individual assets in a portfolio it is possible to construct optimal portfolios, which offer the maximum possible expected return for a given level of risk.
## key insight: an individual asset's return and volatility should not be assessed by itself, but rather by how it contributes to a portfolio's overall return and volatility.
## The optimal portofolios can be plotted on a graph where the line that connects the optimial portfolios will be an upward sloping hyperbola, which is called the Efficient Frontier.
## "Efficient" because the portfolios that lie on it provide the highest expected return for a given level of risk.


#### =============== Extract Stock Prices from Yahoo Finance =============== ####
# Gathering the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas_datareader as dr
from pandas_datareader import data
from datetime import datetime
import cvxopt as opt
from cvxopt import blas, solvers

# Define start and end date
end = datetime(2020, 7, 9)
start = datetime(2015, 8, 6)

# Create a list of the ticker symbols to be used in this project
tickers = ['AMZN', 'GOOGL', 'JNJ', 'V', 'PG', 'UNH', 'JPM', 'HD', 'VZ', 'NFLX', 'DIS', 'MRK', 'PEP', 'BAC', 'KO',
           'WMT','CVX', 'ABT', 'AMGN', 'MCD', 'COST', 'NKE', 'PM', 'QCOM', 'LOW', 'BA', 'LMT', 'SBUX', 'UPS', 'CAT']

# Obtain the adjusted closing prices from Yahoo Finance
prices = pd.DataFrame()
for tick in tickers:
    prices[tick] = data.DataReader(tick, data_source = 'yahoo', start = start, end = end)['Adj Close']
prices.columns = tickers

prices

# Plot the time series
normalised = prices / prices.iloc[0] * 100
normalised.plot(figsize=(20, 10))
plt.title('Stock Time Series 2015 - 2020', fontsize=20)

#--- Mean-Variance Portfolio Allocation
# Calculate the log returns
log_r = np.log(prices / prices.shift(1))

# Compute the annualised returns
annual_r = log_r.mean() * 255
annual_r
# Under the assumptions of independent and identically distributed returns we can also annualise the covariance matrix using trading days.

cov_matrix = log_r.cov() * 255
var = log_r.var() * 255

# Next, I will generate random weights for all of the 30 stocks, which will make up the randomly generated portfolios, under a combination of assumptions. The assumptions are that only long positions are allowed, which ultimately means that the investor's wealth has to be divided among all available stocks through positive positions, and the positions have to add up to 100%, i.e. no additional borrowing and investing more than 100% of wealth.
# Get the total number of stocks used
num_stocks = len(tickers)

# Generate 30 random weights between 0 and 1
weights = np.random.random(num_stocks)

# Constrain these weights to add up to 1
weights /= np.sum(weights)
weights
