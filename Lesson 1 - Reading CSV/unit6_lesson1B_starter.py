"""
Unit 6 - Lesson 1B: Processing CSV Data
========================================
"""

# =============================================================================
# 🔧 LAMBDA QUICK REFERENCE
# =============================================================================

# lambda parameter: what_to_return
#
# Example:
#   lambda p: int(p['wins'])
#
#   Means: "given p, return int(p['wins'])"
#
# Used with max(), min(), sorted():
#   max(players, key=lambda p: int(p['wins']))
#   "Find the player with the highest wins"


# =============================================================================
# 🎯 ACTIVITY 2: Player Statistics Report
# =============================================================================
# Combine all 4 challenges into one statistics report
#
# Print:
# 1. Total number of players
# 2. Total gold across all players
# 3. Player with the most wins
# 4. Average XP per player
#
# Expected output:
# === PLAYER STATISTICS ===
# Total players: 48
# Total gold: 502,300
# Most wins: SpectralGhost (200 wins)
# Average XP: 38,472.9

import csv

with open("players.csv", "r") as file:
    players = list(csv.DictReader(file))

    # TODO: Calculate total_players
    total_players = len(players)
print(f"total players: {total_players}")
print(players)

# TODO: Calculate total_gold
# total_gold = 0
# for player in players:
#     total_gold += int(player["gold"])
# print(f"total gold: {total_gold}")

# One line version
total_gold = sum(int(player["gold"]) for player in players)
print(f"total gold: {total_gold}")  # 584420

# TODO: Calculate avg_xp
total_xp = sum(int(player["xp"]) for player in players)
avg_xp = total_xp / total_players
print(f"total xp: {total_xp}")  # 1933450

# TODO: Find top_player (most wins)
# top_player = None
# most_wins = 0

# for player in players:
#     wins = int(player["wins"])
#     if wins > most_wins:
#         most_wins = wins
#         top_player = player

# One line version
top_player = max(players, key=lambda player: int(player["wins"]))
# print(f"top player: {top_player["username"]} ({top_player["wins"]} wins)")
# SpectralGhost (200 wins)
print()

print("=== PLAYER STATISTICS ===")
# TODO: Print all statistics
print(f"total players: {total_players}")  # 48
print(f"total gold: {total_gold}")  # 584420
print(f"top player: {top_player["username"]} ({top_player["wins"]} wins)")
# SpectralGhost (200 wins)
print(f"average xp: {avg_xp}")  # 40280.208333333336
print()


# =============================================================================
# 🎯 ACTIVITY 3: Player Lookup Tool
# =============================================================================
# Build an interactive player search system
#
# Requirements:
# 1. Load players.csv at the start
# 2. Ask user for a username to search
# 3. If found → display all their stats
# 4. If not found → show error message
# 5. Loop until user types "quit"


# 1. Load function
def load_players(filename):
    # TODO: Load and return list of players
    players = []
    with open(filename, "r") as file:
        # reader = csv.DictReader(file)
        # for row in reader:
        #     players.appened(row)
        return list(csv.DictReader(file))


# 2. Find function
def find_player(players, username):
    # TODO: Loop through players
    for player in players:
        # TODO: Return player if username matches (case-insensitive)
        if player["username"].lower() == username.lower():
            return player
    # TODO: Return None if not found
    return None


# 3. Main program
players = load_players("players.csv")
print(players)
print("=== PLAYER LOOKUP ===")

while True:
    search = input("Enter username (or 'quit'): ")
    # TODO: Check for quit
    if search.lower() == "quit":
        print("Goodbye!")
        break
    # TODO: Search for player
    player = find_player(players, search)
    # TODO: Display results or "not found"
    if player:
        print(f"\nFound Player:")
        print(f"Username: {player["username"]}")
        print(f"Level: {player["level"]}")
        print(f"Xp: {player["xp"]}")
        print(f"Gold: {player["gold"]}")
        print(f"Wins: {player["wins"]}")
    else:
        print(f"\nPlayer '{search}' not found")


# =============================================================================
# 🧪 SANDBOX - Experiment here!
# =============================================================================
