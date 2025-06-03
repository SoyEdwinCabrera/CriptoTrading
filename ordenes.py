from dotenv import load_dotenv
from binance import Client
import os
import datetime as dt
import mplfinance as mpl
import pandas as pd

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
API_KEY = os.getenv('api_key1')
APIE_SECRET = os.getenv('api_secret1')
client = Client(API_KEY, APIE_SECRET)
#price = client.get_symbol_ticker(symbol='BTCUSDT')
# print(price)

price = client.get_symbol_ticker(symbol='ETHUSDT')
print(price)

asset = 'ETHUSDT'
start = "2025.1.1"
end = "2025..6"
timeframe = '1d'
df = pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
df=df.iloc[:,:6]
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
df = df.set_index('Date')
df.index = pd.to_datetime(df.index, unit='ms')
df = df.astype(float)
print(df)
mpl.plot(df,type='candle', volume=True, style='yahoo', mav=7)

# Lanzar orden de compra

# First get ETH price
eth_price = client.get_symbol_ticker(symbol='ETHUSDT')

# Calculate how much ETH to buy with $100
buy_quantity = round(100 / float(eth_price['price']))

# Create test order
order = client.create_test_order(
    symbol='ETHUSDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=buy_quantity
)