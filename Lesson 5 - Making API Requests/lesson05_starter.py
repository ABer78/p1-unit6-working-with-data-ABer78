"""
Unit 6, Lesson 5: Making API Requests — Starter File
======================================================
Today you write Python code that fetches LIVE data from the internet!

The 3-step pattern for every request:
  1. Send the request    →  response = requests.get(url)
  2. Check the status    →  if response.status_code == 200:
  3. Use the data        →  data = response.json()

Make sure you've installed requests:
  pip install requests
"""

import requests


# ============================================================
# EXERCISE 1: Your First API Request
# ============================================================
# Fetch exchange rates for USD and print the status code.
# ============================================================

print("=" * 50)
print("  EXERCISE 1: First Request")
print("=" * 50)

# TODO: Send a GET request to this URL:
#   https://api.exchangerate-api.com/v4/latest/USD
response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")


# TODO: Print the status code
# HINT: response.status_code
print(f"Status code: {response}")  # <Response [200]> (if ok) (Response object)
print(f"Status code: {response.status_code}")  # 200 (if ok)
print(f"Status code: {response.ok}")  # True (if ok)
print()


# ============================================================
# EXERCISE 2: Extract the JSON Data
# ============================================================
# Use .json() to convert the response into a dictionary.
# Then access specific values.
# ============================================================

print("=" * 50)
print("  EXERCISE 2: Get the Data")
print("=" * 50)

# TODO: Parse the response into a dictionary
# HINT: data = response.json()
data = response.json()

# TODO: Print the base currency
# HINT: data["base"]
print(f"Base currency: {data["base"]}")  # USD

# TODO: Print the EUR exchange rate
# HINT: data["rates"]["EUR"]
print(f"1 USD = {data["rates"]["EUR"]} EUR")  # 0.844 EUR

# TODO: Print the JPY exchange rate
print(f"1 USD = {data["rates"]["JPY"]} JPY")  # 153.52 JPY
print()


# ============================================================
# EXERCISE 3: Add the Safety Check
# ============================================================
# Fetch rates for GBP, but only use the data if status is 200.
# ============================================================

print("=" * 50)
print("  EXERCISE 3: Safety Check")
print("=" * 50)

# TODO: Send a GET request for GBP rates
# URL: https://api.exchangerate-api.com/v4/latest/GBP
response2 = requests.get("https://api.exchangerate-api.com/v4/latest/GBP")


# TODO: Check if status_code == 200
#   If yes: parse JSON, print "1 GBP = ??? USD"
#   If no:  print an error message
if response2.status_code == 200:
    data2 = response2.json()
    print(f"1 GBP = {data2["rates"]["USD"]} USD")  # 1.36 USD
else:
    print(f"Error: {response2.status_code}")

print()


# ============================================================
# EXERCISE 4: Fetch Weather with params
# ============================================================
# Use a params dictionary instead of putting everything in the URL.
# ============================================================

print("=" * 50)
print("  EXERCISE 4: Weather with params")
print("=" * 50)

url = "https://api.open-meteo.com/v1/forecast"

# TODO: Create a params dictionary with these keys:
params = {
    "latitude": 40.89,
    "longitude": -74.04,
    "current_weather": True,
    "temperature_unit": "fahrenheit",
}


# TODO: Send request with params
# HINT: requests.get(url, params=params)
response3 = requests.get(url, params=params)

# TODO: Check status, parse JSON, print the temperature
# HINT: weather["current_weather"]["temperature"]
if response3.status_code == 200:
    weather = response3.json()
    print(weather)
    temp = weather["current_weather"]["temperature"]
    wind = weather["current_weather"]["windspeed"]
    print(f"Temp: {temp}")
    print(f"Wind Speed: {wind}")

print()


# ============================================================
# EXERCISE 5: Error Handling
# ============================================================
# Wrap your request in try/except to handle network errors.
# ============================================================

print("=" * 50)
print("  EXERCISE 5: Error Handling")
print("=" * 50)

# TODO: Use try/except to safely fetch exchange rates
# Catch these exceptions:
#   requests.exceptions.Timeout
#   requests.exceptions.ConnectionError

# TEMPLATE:
# try:
#     response = requests.get(url, timeout=5)
#     if response.status_code == 200:
#         data = response.json()
#         print(f"1 USD = {data['rates']['EUR']} EUR")
#     else:
#         print(f"API error: {response.status_code}")
# except requests.exceptions.Timeout:
#     print("Request timed out!")
# except requests.exceptions.ConnectionError:
#     print("No internet connection!")

print("(Complete the try/except above)")
print()


# ============================================================
# EXERCISE 6: Build a Reusable Function
# ============================================================
# Create a function that fetches country info from REST Countries.
# ============================================================

print("=" * 50)
print("  EXERCISE 6: Build a Function")
print("=" * 50)


def get_country_info(country_name):
    """Fetch country data from REST Countries API.

    Args:
        country_name: Name of the country (e.g., "japan")

    Returns:
        Dictionary with country info, or None if request fails.
    """
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    params = {"fields": "name,capital,currencies,population"}

    # TODO: Send request with params and timeout=5

    # TODO: Check status code == 200

    # TODO: Parse JSON and return data[0]
    #   (The API returns a list — we want the first item)

    # TODO: Return None if anything goes wrong

    return None  # Replace with your code


# Test your function:
info = get_country_info("japan")
if info:
    print(f"Country: {info['name']['common']}")
    print(f"Capital: {info['capital'][0]}")
else:
    print("Could not fetch country data.")
print()
