# =============================================================================
# 🎯 Homework: Give Everyone Gold!
# =============================================================================
# Load players.csv, add 500 gold to each player, save it back.
#
# Steps:
# 1. READ - Load all players
# 2. MODIFY - Add 500 to each player's gold
# 3. WRITE - Save back to the file

# YOUR CODE HERE:

# 1. READ
import csv

with open("players.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    data = list(reader)

# 2. MODIFY
    for row in data:
        current_gold = int(row[3])
        row[3] = current_gold + 500

# 3. WRITE
with open("players.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)