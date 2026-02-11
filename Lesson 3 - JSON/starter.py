"""Unit 6 - Lesson 3: Working with JSON"""

import json


# =============================================================================
# 🎯 ACTIVITY 1: Read and Analyze Customer Data
# =============================================================================
# Load customer_data.json and find the highest-spending customer
#
# Expected output:
# Top customer: TechStart Inc
# Total spent: $72,000

# YOUR CODE HERE:
import json

# Load the JSON file
with open("customer_data.json", "r") as file:
    customers = json.load(file)
    print(type(customers))  # <class 'list'> (list of dictionaries)
    print(type(customers[0]["total_spent"]))  # <class 'int'>
# Find the highest spender
highest_spender = customers[0]
# print(highest_spender)
for customer in customers:
    if customer["total_spent"] > highest_spender["total_spent"]:
        highest_spender = customer

# Display the results
print(f"Top Customer: {highest_spender["name"]}")  # TechStart Inc
print(f"Top Customer: ${highest_spender["total_spent"]:,}")  # $72,000
print()

# =============================================================================
# 🎯 ACTIVITY 2: Create Product Catalog
# =============================================================================
# Create a product catalog and save it as JSON
#
# Products to include:
# - Wireless Mouse ($29.99, Electronics)
# - USB Cable ($12.99, Accessories)
# - Laptop Stand ($45.00, Furniture)

products = [
    {"id": "P001", "name": "Wireless Mouse", "price": 29.99, "category": "Electronics"},
    {"id": "P002", "name": "USB Cable", "price": 12.99, "category": "Accessories"},
    {"id": "P003", "name": "Laptop Stand", "price": 45.00, "category": "Furniture"},
]

# YOUR CODE HERE:
# 1. Write products to "catalog.json" with indent=4
with open("catalog.json", "w") as file:
    json.dump(products, file, indent=4)
print("Catalog created")

# 2. Read it back and print all product names
with open("catalog.json", "r") as file:
    loaded_products = json.load(file)
print("\nproducts in catalog:")
for product in loaded_products:
    print(f" - {product["name"]}")
print()

# =============================================================================
# 🔤 PRACTICE: JSON Strings
# =============================================================================
# Practice with json.loads() and json.dumps()

import json

# Parse this JSON string from an "API response"
api_response = '{"status": "success", "revenue": 45000, "customers": 127}'

# YOUR CODE HERE:
# 1. Parse the string into a Python dictionary
data = json.load(api_response)  # converts to dictionary
# print(type(data))

import requests

url = "https://jsonplaceholdertyp1code.com/todos/1"
response = requests.get(url)  # if successful we get 200 status code
response_data = response.json()  # converts json string to dictionary
print(f"{type(response_data)}")

# 2. Print the revenue
print(f"Revenue: ${data.get("revenue", 0)}")

# 3. Convert back to a formatted JSON string
formatted_json = json.dumps(data, indent=4)
print("Formatted string")
print(formatted_json)


# =============================================================================
# 🏢 PRACTICE: Nested Data
# =============================================================================
# Work with nested JSON structures

company = {
    "name": "TechCorp",
    "founded": 2018,
    "location": {"city": "San Francisco", "state": "CA", "zip": "94105"},
    "departments": ["Sales", "IT", "Marketing", "Finance"],
}

# YOUR CODE HERE:
# 1. Print the city
print(f"City: {company["location"]["city"]}")  # San Francisco

# 2. Print the first department
print(f"Department: {company["departments"][1]}")

# 3. Save this to "company_info.json"
