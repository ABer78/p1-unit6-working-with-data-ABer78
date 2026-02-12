"""
Unit 6, Lesson 4: Introduction to APIs — Starter File
=======================================================
No internet requests today — just understanding how APIs work!
We'll use the json module you already know from Lesson 3.
"""

import json


# ============================================================
# EXERCISE 1: Identify the Parts of an API URL
# ============================================================
# Look at each URL and fill in the parts as strings.
#
# REMINDER:
#   base_url   = the server (https://something.com)
#   endpoint   = the path (/v1/something)
#   parameters = key=value pairs after the ?
# ============================================================

print("=" * 50)
print("  EXERCISE 1: URL Parts")
print("=" * 50)

# URL: https://api.exchangerate-api.com/v4/latest/USD

url_base = ""  # TODO: What is the base URL?
url_endpoint = ""  # TODO: What is the endpoint?
url_parameter = ""  # TODO: What specific data is requested?

print(f"Base URL:  {url_base}")
print(f"Endpoint:  {url_endpoint}")
print(f"Parameter: {url_parameter}")
print()


# ============================================================
# EXERCISE 2: Predict the Status Code
# ============================================================
# Common codes:
#   200 = OK (success!)
#   401 = Unauthorized (need a key)
#   404 = Not Found (doesn't exist)
#   500 = Server Error (not your fault)
# ============================================================

print("=" * 50)
print("  EXERCISE 2: Status Codes")
print("=" * 50)

# A: Requesting exchange rates for USD (a real currency)
answer_a = 0  # TODO: What status code?

# B: Requesting exchange rates for "FAKEMONEY"
answer_b = 0  # TODO: What status code?

# C: Accessing Stripe's API without an API key
answer_c = 0  # TODO: What status code?

print(f"A) Valid currency (USD):   {answer_a}")
print(f"B) Fake currency:          {answer_b}")
print(f"C) No API key on Stripe:   {answer_c}")
print()


# ============================================================
# EXERCISE 3: Parse Exchange Rate JSON
# ============================================================
# Pretend this JSON came from the ExchangeRate API.
# Use json.loads() to parse it, then answer the questions.
# ============================================================

print("=" * 50)
print("  EXERCISE 3: Exchange Rate Data")
print("=" * 50)

exchange_json = """
{
    "base": "USD",
    "date": "2025-02-10",
    "rates": {
        "EUR": 0.96,
        "GBP": 0.80,
        "JPY": 151.85,
        "CAD": 1.44,
        "MXN": 20.45
    }
}
"""

# TODO: Parse the JSON string into a Python dictionary
data = json.loads(exchange_json)

# TODO: Print the base currency
print(f"Base currency: {data["base"]}")

# TODO: Print the EUR rate
print(f"1 USD = {data["rates"]["EUR"]} EUR")

# TODO: Print the JPY rate
print(f"1 USD = {data["rates"]["JPY"]} JPY")

# TODO: How many currencies are listed?
print(f"Number of currencies: {len(data["rates"])}")
print()


# ============================================================
# EXERCISE 4: Parse Country JSON
# ============================================================
# This is what the REST Countries API returns for Germany.
# Careful — the outer structure is a LIST [ ], not a dict { }
# ============================================================

print("=" * 50)
print("  EXERCISE 4: Country Data")
print("=" * 50)

country_json = """
[
    {
        "name": {
            "common": "Germany",
            "official": "Federal Republic of Germany"
        },
        "capital": ["Berlin"],
        "currencies": {
            "EUR": {
                "name": "Euro",
                "symbol": "€"
            }
        }
    }
]
"""

# TODO: Parse the JSON string
country_list = None  # Replace None

# TODO: Get the first (only) country from the list
# HINT: It's a list, so use [0]
country = None

# TODO: Print the common name
# HINT: country["name"]["common"]
print(f"Country: ???")

# TODO: Print the capital
# HINT: country["capital"] is a list — use [0]
print(f"Capital: ???")

# TODO: Print the currency name
# HINT: country["currencies"]["EUR"]["name"]
print(f"Currency: ???")
print()


# ============================================================
# EXERCISE 5: Parse Weather JSON
# ============================================================
# This is what Open-Meteo returns for a weather request.
# ============================================================

print("=" * 50)
print("  EXERCISE 5: Weather Data")
print("=" * 50)

weather_json = """
{
    "current_weather": {
        "temperature": 42.5,
        "windspeed": 8.3,
        "time": "2025-02-10T14:00"
    },
    "current_weather_units": {
        "temperature": "°F",
        "windspeed": "mph"
    }
}
"""

# TODO: Parse the JSON string
weather = None  # Replace None

# TODO: Print the temperature with its unit
# HINT: weather["current_weather"]["temperature"]
# HINT: weather["current_weather_units"]["temperature"]
print(f"Temperature: ???")

# TODO: Print the wind speed with its unit
print(f"Wind speed: ???")
print()


# ============================================================
# EXERCISE 6: Build API URLs
# ============================================================
# Combine variables into complete API URLs using f-strings.
# This previews what we'll do in Lesson 5!
# ============================================================

print("=" * 50)
print("  EXERCISE 6: Build URLs")
print("=" * 50)

# Build: https://api.exchangerate-api.com/v4/latest/EUR
base = "https://api.exchangerate-api.com"
currency = "EUR"

# TODO: Create the full URL with an f-string
url = ""  # TODO: f"{base}/v4/latest/{currency}"
print(f"URL: {url}")

# Build: https://restcountries.com/v3.1/name/brazil
country_base = "https://restcountries.com"
country_name = "brazil"

# TODO: Create the full URL
country_url = ""  # TODO
print(f"URL: {country_url}")
print()


# ============================================================
# BONUS: Simple Currency Converter
# ============================================================
# Use the exchange rate data from Exercise 3 to convert $100
# to Japanese Yen. Preview of what we'll build with LIVE data!
# ============================================================

print("=" * 50)
print("  BONUS: Currency Converter")
print("=" * 50)

usd_amount = 100
target = "JPY"

# TODO: Get the rate from the data dictionary (Exercise 3)
# HINT: rate = data["rates"][target]
# TODO: Calculate: converted = usd_amount * rate
# TODO: Print the result with formatting

print(f"${usd_amount} USD = ??? {target}")
print()

print("=" * 50)
print("  Lesson 4 complete!")
print("  Next: We'll fetch LIVE data with Python! 🚀")
print("=" * 50)
