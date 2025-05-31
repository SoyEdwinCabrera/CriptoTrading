import yfinance as yf
import pandas as pd
import json, requests

def Gold():
    gold = yf.Ticker("GC=F").history(period="1y")
    gold.to_csv('GOLD.csv', encoding='utf-8')
    print(gold)
    print("Extration finished sp500 😀")
Gold()

url = "https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD"
response = requests.get(url)

gold = response.json()
data = gold[0]
dataclean = data["spreadProfilePrices"]
datafinish = dataclean[0]["ask"]
print("El precio del oro hoy es = " + str(datafinish) + " USD")


# # Verifica si la solicitud fue exitosa
# if response.status_code == 200:
#     try:
#         # Intenta cargar el contenido como JSON
#         gold = response.json()
#         print(gold)
#     except json.JSONDecodeError as e:
#         print(f"Error al decodificar JSON: {e}")
# else:
#     print(f"Error en la solicitud: {response.status_code}")