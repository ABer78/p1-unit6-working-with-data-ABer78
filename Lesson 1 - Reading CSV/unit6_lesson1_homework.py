# =============================================================================
# 🎯 ACTIVITY 1: Load and Display
# =============================================================================
# Print each player's stats in this format:
# === PLAYER ROSTER ===
# DragonSlayer99 | Level 25 | 42 wins
# CoolCat2024 | Level 12 | 15 wins
import csv

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row["username"]} | Level {row["level"]} | {row["wins"]} wins")


# =============================================================================
# 🎯 ACTIVITY 2: Player Statistics
# =============================================================================
# Calculate and print:
# - Total number of players
# - Total gold across all players
# - Player with the most wins
# - Average XP per player
import csv

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    total = 0
    gold = 0
    wins = 0
    xp = 0
    avg_xp = 0
    most_wins = ""
    for row in reader:
        total += 1
        gold += row["gold"]
        xp += row["xp"]
        if row["wins"] > wins:
            wins = row["wins"]
            most_wins = row["username"]
    avg_xp = xp / total
    print(
        f"Total players: {total}, Total gold: {gold}, Most wins: {most_wins} ({wins} wins), Average XP: {avg_xp}"
    )
