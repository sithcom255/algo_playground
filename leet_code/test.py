import sys
import ccxt
import talib

# Load the exchange and set the API key and secret
exchange = ccxt.by_it({
    'apiKey': 'F60hKhJvkmT3HhGndZ',
    'secret': 'CUCuTBbl8I6oDX5gaEbKlET13UbMhV4RB3j3'
})

# Set the symbol for the OP coin (perpetuals contract)
symbol = 'OP/USDT'

# Set the timeframe to 5 minutes
timeframe = '5m'

# Retrieve the 4 hour OHLCV data for the OP coin
ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

# Extract the close prices from the OHLCV data
close_prices = [x[4] for x in ohlcv]

# Calculate the 34 EMA of the close prices
ema = talib.EMA(close_prices, timeperiod=34)

# Get the current price of the OP coin
price = exchange.fetch_ticker(symbol)['last']

# If the price touches the EMA, place a short order with 10x leverage
if price >= ema:
    order = exchange.create_order(symbol, 'market', 'sell', 1, {'leverage': 10})