"""
Unit 6 Lesson 1 Homework: Movie Database Analytics

Practice the essential CSV skills:
  1. Load CSV with DictReader
  2. Access data by column name
  3. Convert strings to numbers
  4. Calculate statistics
"""

import csv

print("🎬 Movie Database Analytics 🎬")
print("=" * 35)
print()


# ============================================
# ✅ TASK 1: Load and Display (DICTREADER)
# ============================================
# Load movies.csv and print each movie's title, year, and rating.
#
# Expected output:
# === MOVIE DATABASE ===
# The Dark Knight (2008) - Rating: 9.0
# Inception (2010) - Rating: 8.8
# ...
#
# PATTERN REMINDER:
#   with open("movies.csv", "r") as file:
#       reader = csv.DictReader(file)
#       for row in reader:
#           print(row['column_name'])

print("--- Task 1: Movie List ---")

# YOUR CODE HERE:
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"]
        year = row["year"]
        rating = row["rating"]
        print(f"{title} ({year}) - Rating: {rating}")


# ============================================
# ✅ TASK 2: Total Revenue (SUM PATTERN)
# ============================================
# Calculate the total box office revenue of all movies.
#
# Expected output: "Total box office revenue: $4,414 million"
#
# ⚠️ REMEMBER: CSV values are STRINGS! Use int() to convert.
#
# PATTERN REMINDER:
#   total = 0
#   for row in reader:
#       total += int(row['revenue'])

print()
print("--- Task 2: Total Revenue ---")

# YOUR CODE HERE:
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)

    total = 0
    for row in reader:
        total += int(row["revenue"])
    print(f"Total box office revenue: ${total:,} million")


# ============================================
# ✅ TASK 3: Count Top-Rated (COUNT PATTERN)
# ============================================
# Count how many movies have a rating of 8.8 or higher.
#
# Expected output: "Highly rated movies (8.8+): 5 movies"
#
# ⚠️ REMEMBER: Use float() for decimal numbers!
#
# PATTERN REMINDER:
#   count = 0
#   for row in reader:
#       if float(row['rating']) >= 8.8:
#           count += 1

print()
print("--- Task 3: Count Top-Rated ---")

# YOUR CODE HERE:
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)

    count = 0
    for row in reader:
        if float(row["rating"]) >= 8.8:
            count += 1
    print(f"Highly rated movies (8.8+): {count} movies")


# ============================================
# ✅ TASK 4: Find Highest Rated (FIND BEST)
# ============================================
# Find the movie with the highest rating.
#
# Expected output: "Highest rated: The Godfather (9.2)"
#
# 💡 HINT: Load into a list first, then loop to find best.
#
# PATTERN REMINDER:
#   movies = list(csv.DictReader(file))
#   best = movies[0]
#   for movie in movies:
#       if float(movie['rating']) > float(best['rating']):
#           best = movie

print()
print("--- Task 4: Highest Rated ---")

# YOUR CODE HERE:
with open("movies.csv", "r") as file:
    movies = list(csv.DictReader(file))

best = movies[0]
for movie in movies:
    if float(movie["rating"]) > float(best["rating"]):
        best = movie
print(f"Highest rated: {best["title"]} ({best["rating"]})")


# ============================================
# 🌟 BONUS: Find Oldest Movie
# ============================================
# Find the movie with the smallest year (oldest).
#
# Expected output: "Oldest movie: The Godfather (1972)"
#
# 💡 HINT: Same pattern as Task 4, but use < instead of >

print()
print("--- BONUS: Oldest Movie ---")

# YOUR CODE HERE:
with open("movies.csv", "r") as file:
    movies = list(csv.DictReader(file))

oldest = movies[0]
for movie in movies:
    if float(movie["year"]) < float(oldest["year"]):
        oldest = movie
print(f"Oldest Movie: {oldest["title"]} ({oldest["rating"]})")


# ============================================
# 🎉 END OF HOMEWORK
# ============================================
print()
print("=" * 35)
print("🎬 Homework Complete! Great job! 🎬")
