import sys
import json
import requests


if len(sys.argv) != 2:
    sys.exit("Too Less/Much Arguments!")

n = None

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# 'Trying' Getting Data
bitcoin_index = None

try:
    bitcoin_index = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json"
    ).json()
except requests.RequestException:
    sys.exit("API Issue, Try Again Later!")

# Extracting Price from it
bitcoin_price = bitcoin_index["bpi"]["USD"]["rate_float"]

print(f"${bitcoin_price * n:,.4f}", end="")
