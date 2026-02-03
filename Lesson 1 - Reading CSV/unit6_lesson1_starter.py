"""Unit 6 - Lesson 2: Reading CSV Files"""

# import csv

# =============================================================================
# 📚 SYNTAX REFERENCE
# =============================================================================

# --- Opening and Reading with DictReader ---
#
# with open("filename.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['column_name'])
#
# --- Loading All Data into a List ---
#
# with open("filename.csv", "r") as file:
#     data = list(csv.DictReader(file))
#

# =============================================================================
# ⚠️ KEY RULES TO REMEMBER
# =============================================================================

# 1. ALL CSV VALUES ARE STRINGS!
#    Even numbers like "25" come in as strings
#    Convert when needed: int(row['level']) or float(row['price'])

# 2. DictReader uses the FIRST ROW as keys
#    No need to skip headers - it's automatic

# 3. The file CLOSES after the "with" block
#    Load into a list if you need data later: data = list(reader)

# 4. Column names are CASE-SENSITIVE
#    row['Username'] ≠ row['username']


# csv.reader - Basic Usage
import csv

with open("players.csv", "r") as file:
    reader = csv.reader(file)
    # print(reader) # <_csv.reader object at 0x0000022494A5E4A0>
    # print(type(reader)) # <class "_csv.reader">
    # header = next(reader) # skips header row
    # print(header) # ["username", "level", "xp", "gold", "wins"]
    for row in reader:
        # print(row)
        # print(type(row)) # <class "list">
        username = row[0]
        level = row[1]
        print(f"{username} is level {level}")


# csv.DictReader - Better Way
import csv

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(row)
        print(f"{row["username"]} is level {row["level"]}")


# =============================================================================
# 🎯 ACTIVITY 1: Load and Display
# =============================================================================
# Print each player's stats in this format:
# === PLAYER ROSTER ===
# DragonSlayer99 | Level 25 | 42 wins
# CoolCat2024 | Level 12 | 15 wins
# ...


# =============================================================================
# 🎯 ACTIVITY 2: Player Statistics
# =============================================================================
# Calculate and print:
# - Total number of players
# - Total gold across all players
# - Player with the most wins
# - Average XP per player


# =============================================================================
# 🎯 ACTIVITY 3: Player Lookup Tool
# =============================================================================
# Interactive search:
# - Ask user for username
# - Display their stats if found
# - Show error if not found
# - Loop until user types "quit"
