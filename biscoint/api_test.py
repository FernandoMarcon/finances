# Source
# https://pypi.org/project/biscoint-api-python/
# https://github.com/Biscoint/biscoint-api-python

import json
import requests

from biscoint_api_python import Biscoint

api_data = {
    'api_key': '3ddc931bf25c94ff0344a2e409aa37339e400b8d4da72265f97c3a31d0cfb36e',
    'api_secret': 'd4c4db1567fba7dbc63b73e0a5c3a810360825a1de4530e05a77652efce91bcb',
}

bsc = Biscoint(api_data['api_key'], api_data['api_secret'])

try:
    ticker = bsc.get_ticker()
    print(json.dumps(ticker, indent=4))

    fees = bsc.get_fees()
    print(json.dumps(fees, indent=4))

    meta = bsc.get_meta()
    print(json.dumps(meta, indent=4))

    balance = bsc.get_balance()
    print(json.dumps(balance, indent=4

    trades = bsc.get_trades(op='buy', length=1)
    print(json.dumps(trades, indent=4

    offer = bsc.get_offer('buy', '0.002', False)
    print(json.dumps(offer, indent=4))

    # WARNING: this will actually execute the buy operation!
    offerConfirmation = bsc.confirm_offer(offer['offerId'])
    print(json.dumps(offerConfirmation, indent=4))

except requests.exceptions.HTTPError as error:
    print(error)
    print(json.dumps(error.response.json(), indent=4))
