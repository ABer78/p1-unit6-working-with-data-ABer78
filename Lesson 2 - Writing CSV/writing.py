"""
Unit 6 - Lesson 2: Writing CSV Files
=====================================
📌 Keep this open as a reference while following the slides!
"""

import csv

# =============================================================================
# 📚 SYNTAX REFERENCE
# =============================================================================

# --- Create New CSV File (Write Mode) ---
#
# with open("filename.csv", "w", newline="") as file:
#     fieldnames = ['col1', 'col2', 'col3']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()      # Write column names
#     writer.writerows(data)    # Write all rows
#

# --- Add to Existing CSV (Append Mode) ---
#
# with open("filename.csv", "a", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writerow(single_record)   # NO header!
#


# =============================================================================
# 🎯 ACTIVITY 1: Create a Scores File
# =============================================================================
# Create a file called "high_scores.csv" with game scores.
#
# Expected file contents:
# player,game,score
# Alice,Tetris,15000
# Bob,Snake,8500
# Charlie,Tetris,12000

scores = [
    {"player": "Alice", "game": "Tetris", "score": 15000},
    {"player": "Bob", "game": "Snake", "score": 8500},
    {"player": "Charlie", "game": "Tetris", "score": 12000},
]

new_score = {"player": "Carl", "game": "Puyo Puyo", "score": "16000"}

# YOUR CODE HERE:
with open("high_scores.csv", "w", newline="") as file:
    # 1 - Define the column names
    fieldnames = ["player", "game", "score"]
    # 2 - Create the write with columns
    writer = csv.DictWriter(file, fieldnames)
    # 3 - Write the header row
    writer.writeheader()
    # 4 - Write all data rows
    # 4.1 - writerow() one at a time
    # for score in scores:
    #     writer.writerow(score)
    # 4.2 - writerows() all at once
    writer.writerows(scores)

with open("high_scores.csv", "a", newline="") as file:
    fieldnames = ["player", "game", "score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow(new_score)
print("New score added!")
print()


# =============================================================================
# 🎯 ACTIVITY 2: Add Score Function
# =============================================================================
# Create a function that adds a new score to high_scores.csv
#
# Test with:
# add_score("Eve", "Tetris", 18000)
# add_score("Frank", "Snake", 7200)


def add_score(player, game, score):
    """Add a new score to the high scores file."""
    # TODO: Create the new_score dictionary
    new_score2 = {"player": player, "game": game, "score": score}
    # TODO: Open file in APPEND mode
    with open("high_scores.csv", "a", newline="") as file:
        # TODO: Create DictWriter with fieldnames
        fieldnames = ["player", "game", "score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # TODO: Write the single row (NO header!)
        writer.writerow(new_score2)

    # TODO: Print confirmation
    print(f"Score added: {player}, {game}, {score}")


# Test it:
add_score("Eve", "Tetris", 18000)
add_score("Frank", "Snake", 7200)


# =============================================================================
# 🎯 ACTIVITY 3: Give Everyone Gold!
# =============================================================================
# Load players.csv, add 500 gold to each player, save it back.
#
# Steps:
# 1. READ - Load all players
# 2. MODIFY - Add 500 to each player's gold
# 3. WRITE - Save back to the file

# YOUR CODE HERE:

# 1. READ


# 2. MODIFY


# 3. WRITE
