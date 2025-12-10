import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try :
    float(sys.argv[1])
except ValueError :
    sys.exit("Command-line argument is not a number")


response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=444f0e9b99bb4b487fac3cb8fdeeb964d93b23e73dc46b8cd25fee8fd10915f3")

results = response.json()
data = results["data"]

total_price = float(sys.argv[1]) * float(data["priceUsd"])

print (f"${total_price:,.4f}")
