import pandas as pd
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import sys
sys.path.insert(1, '/home/marcon/Documents/exchange/')
import config

# Authenticate
client = Client(config.API_KEY, config.API_SECRET)

# Account Balance
def getBTC():
    balance = client.get_asset_balance('BTC')['free']
    return float(balance)

def getUSDT():
    balance = client.get_asset_balance('USDT')['free']
    return float(balance)

# Buy/Sell
def buy(symbol = 'BTCUSDT', quant = 100):
    order = client.order_market_buy(symbol=symbol,quantity=quant)
    return order

def sell(symbol = 'BTCUSDT'):
    quant = getBTC()
    order = client.order_market_sell(symbol=symbol,quantity=quant)
    return order

# # Get Balance
# from binance.enums import *
# order = client.create_test_order(
#     symbol='BTCUSDT',
#     side=SIDE_BUY,
#     type=ORDER_TYPE_LIMIT,
#     timeInForce=TIME_IN_FORCE_GTC,
#     quantity=100,
#     price='0.00001')

getUSDT()
