#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     06/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests

# User input
from_currency = input("Enter the currency you would like to convert from: ").upper()
to_currency = input("Enter the currency you would like to convert to: ").upper()
amount = float(input("Enter the amount to convert: "))

# API Key (Replace with your key)
api_key = "6861d2c714c4b15968d51e01"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

# Make API request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    # Check if the target currency exists in the response
    if to_currency in data["conversion_rates"]:
        exchange_rate = data["conversion_rates"][to_currency]
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency code. Please check and try again.")
else:
    print(f"Error: Unable to fetch exchange rates (Status Code: {response.status_code})")


