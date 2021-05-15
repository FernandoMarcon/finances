[source](https://www.youtube.com/playlist?list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay)

## Packages
* wscat

## Links
* [Binance API documentation](https://github.com/binance/binance-spot-api-docs)
* [UnixTimestamp](https://www.unixtimestamp.com/)

## WebSocket
* The base endpoint is: wss://stream.binance.com:9443
* Stream Name: <symbol>@kline_<interval>


wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade
< {"e":"trade","E":1621089898653,"s":"BTCUSDT","t":834947093,"p":"49265.40000000","q":"0.00200000","b":5928744445,"a":5928744784,"T":1621089898652,"m":true,"M":true}

wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_1m
< {"e":"kline","E":1621090322026,"s":"BTCUSDT","k":{"t":1621090320000,"T":1621090379999,"s":"BTCUSDT","i":"1m","f":834966265,"L":834966396,"o":"49583.96000000","c":"49554.55000000","h":"49601.31000000","l":"49554.54000000","v":"4.68721500","n":132,"x":false,"q":"232334.46836387","V":"0.90444200","Q":"44824.30417034","B":"0"}}
