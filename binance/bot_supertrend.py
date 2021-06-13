import pandas as pd
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import sys
sys.path.insert(1, '/home/marcon/Documents/exchange/')
import config

# Authenticate
client = Client(config.API_KEY, config.API_SECRET)

# Settings
symbol = 'BTCUSDT'

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
client.get_account()
client.get_asset_details()['BTC']
client.get_asset_dividend_history()
client.get_trade_fee(symbol='BTCUSDT')
fees = pd.DataFrame(client.get_trade_fee()).set_index('symbol')
fees.loc['BTCUSDT']
fees.head()
interval = client.KLINE_INTERVAL_15MINUTE
since = "1 day ago UTC"

historical_data.head()

def get_data(symbol, interval, since):
    hist_df=pd.DataFrame(client.get_historical_klines(symbol,interval, since),
                        columns = ['Open Time','Open','High','Low','Close','Volume','Close Time','Quote Asset Volume',
                                            'Number of Trades','TB Base Volume','TB Quote Volume','Ignore'])

    hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time']/1000, unit = 's')
    hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time']/1000, unit = 's')
    numeric_columns = ['Open','High','Low','Close','Volume','Quote Asset Volume','TB Base Volume','TB Quote Volume']
    hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)

    return hist_df

data = get_data(symbol, interval, since)
data.head()
data.tail()

# Viz
import mplfinance as mpf
mpf.plot(data.set_index('Close Time'),
        type = 'candle',style='charles',volume=True,
        title = 'BTCUSDT Last 30 Min', mav = (10,20,30))
        
