from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
API_KEY = os.getenv('api_key1')
API_SECRET = os.getenv('api_secret1')


from datetime import date, timedelta
import pandas as pd
from binance import Client
today = date.today()
yesterday = today - timedelta(days=1)

def criptodata(dataticker):
    api_key = API_KEY
    api_secret = API_SECRET
    client = Client(api_key, api_secret)
    price = client.get_symbol_ticker(symbol=dataticker)
    print(price)
    asset = dataticker
    start = "2021.01.01"
    end = str(yesterday)
    timeframe = "1d"
    df = pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
    df = df.iloc[:, 0:6]
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype('float')
    print(df)    
    
    #save to csv
    df.to_csv(dataticker + '.csv', encoding='utf-8')
    print("Data extraction finished 😀")
list = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "LTCUSDT"]
for i in list:
    criptodata(i)
criptodata('BTCUSDT')