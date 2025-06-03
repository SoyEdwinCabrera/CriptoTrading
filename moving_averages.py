"""
MOVING AVERAGES are a tecchnical indicator used in the stock market 
to smooth volability and identify trends in the price of an asset.
They are averages of prices over a given period of time
"""

import pandas as pd

df = pd.read_csv("ETHUSDT.csv")

# Get the last 30 prices
last_30_prices = df["Close"].tail(7)

# Calculate the mean of the last 30 prices
mean_price = last_30_prices.mean()

# Calculate the standard deviation of the last_30_prices
std_price = last_30_prices.std()

# Calculate the support and resistance levels
support_price = mean_price - std_price
resistance_price = mean_price + std_price

# Get the last price
last_price = df["Close"].iloc[-1]

# Compare the last price with the support and resistance levels
if last_price > resistance_price:
    status = "resistance"
    difference = last_price - resistance_price
elif last_price < support_price:
    status = "support"
    difference = support_price - last_price
else:
    status = "neutral"
    difference = 0
    
# Print the results
print(f"The last price({last_price}) is {status} with a difference of {difference}")

if status=="resistance":
    print("Send order to Sell")
elif status=="support":
    print("Send order Buy")
else:
    print("Hold/Do nothing")
