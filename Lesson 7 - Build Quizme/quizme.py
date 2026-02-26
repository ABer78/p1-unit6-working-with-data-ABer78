"""
Lesson 7: QuizMe — AI-Powered Quiz Generator (SOLUTION)
=========================================================
This program:
- Takes study notes from the user
- Uses AI to generate quiz questions
- Runs a multiple-choice quiz (A, B, C, D)
- Saves detailed results to a CSV file next to the exe/py

TO PACKAGE:
  pyinstaller --onefile quizme_solution.py
"""

# ============================================================
# IMPORTS
# ============================================================
import requests
import json
import csv
import os
import sys  # needed for PyInstaller path handling
from datetime import datetime

# ============================================================
# YOUR API KEY (REQUIRED)
# ============================================================
API_KEY = "AIzaSyB5yFL-QJK3Kk_ov5CSabY6EPQykj8nhjk"

URL = (
    "https://generativelanguage.googleapis.com"
    "/v1beta/models/gemini-2.5-flash:generateContent"
    f"?key={API_KEY}"
)

# ============================================================
# STEP 0: HANDLE PATHS FOR PYINSTALLER
# ============================================================


def get_base_dir():
    """
    Returns the folder where the program is running:
    - If running as .py, it's the script folder
    - If running as .exe (PyInstaller), it's the exe folder
    """
    if getattr(sys, "frozen", False):
        # Running in PyInstaller bundle
        return os.path.dirname(sys.executable)
    else:
        # Running as normal .py script
        return os.path.dirname(os.path.abspath(__file__))


# ============================================================
# STEP 1: GET STUDY NOTES FROM THE USER
# ============================================================


def get_notes():
    """
    Collect multi-line notes from the user.
    The user types END on a new line to finish.
    """
    print("Paste your notes (type END on a new line when done):\n")
    lines = []

    while True:
        line = input("> ")
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


# ============================================================
# STEP 2: GENERATE QUIZ USING GEMINI
# ============================================================


def generate_quiz(notes, num_questions=3):
    """
    Sends the user's notes to Gemini and asks it to return
    multiple-choice questions in a strict JSON format (A-D).
    """
    prompt = f"""Based on these study notes, generate exactly \
{num_questions} multiple choice questions.

Each question MUST have exactly four choices labeled A, B, C, and D.

NOTES:
{notes}

Respond with ONLY a valid JSON array in this exact format:
[
  {{
    "question": "What is...?",
    "choices": ["A) ...", "B) ...", "C) ...", "D) ..."],
    "answer": "A"
  }}
]
Only the JSON array. No extra text.
"""

    body = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(URL, json=body, timeout=30)

        if response.status_code != 200:
            print(f"API error: {response.status_code}")
            return None

        data = response.json()

        # Extract the text response from Gemini
        text = data["candidates"][0]["content"]["parts"][0]["text"].strip()

        # Remove ```json code blocks if Gemini adds them
        if text.startswith("```"):
            text = text.split("\n", 1)[1]
            text = text.rsplit("```", 1)[0]

        # Convert JSON text into Python list
        return json.loads(text)

    except Exception as e:
        print("Error generating quiz:", e)
        return None


# ============================================================
# STEP 3: RUN THE QUIZ
# ============================================================


def run_quiz(questions):
    """
    Displays questions to the user, checks answers,
    and collects detailed results for saving.
    """
    score = 0
    total = len(questions)
    results = []

    for i, q in enumerate(questions, 1):
        print(f"\n--- Question {i} of {total} ---")
        print(q["question"])

        # Display all answer choices
        for choice in q["choices"]:
            print(f"  {choice}")

        # Get user's answer
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        correct_answer = q["answer"]

        # Check correctness
        is_correct = user_answer == correct_answer

        if is_correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong — the answer was {correct_answer}")

        # Remove "A) ", "B) ", etc. from choices for clean CSV columns
        choice_a = q["choices"][0][3:]
        choice_b = q["choices"][1][3:]
        choice_c = q["choices"][2][3:]
        choice_d = q["choices"][3][3:]

        # Store detailed result for this question
        results.append(
            {
                "question": q["question"],
                "choice_a": choice_a,
                "choice_b": choice_b,
                "choice_c": choice_c,
                "choice_d": choice_d,
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "result": "Correct" if is_correct else "Wrong",
            }
        )

    print(f"\nScore: {score}/{total} ({score / total * 100:.0f}%)")
    return score, total, results


# ============================================================
# STEP 4: SAVE RESULTS TO CSV
# ============================================================


def save_score(score, total, results):
    """
    Saves quiz results to scores.csv next to the exe/script.
    One row is written for EACH question.
    """
    base_dir = get_base_dir()
    file_path = os.path.join(base_dir, "scores.csv")

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "date",
                "question",
                "choice_a",
                "choice_b",
                "choice_c",
                "choice_d",
                "user_answer",
                "correct_answer",
                "result",
                "score",
                "total",
                "percent",
            ],
        )

        # Write header only once
        if not file_exists:
            writer.writeheader()

        # Write one row per question
        for r in results:
            writer.writerow(
                {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "question": r["question"],
                    "choice_a": r["choice_a"],
                    "choice_b": r["choice_b"],
                    "choice_c": r["choice_c"],
                    "choice_d": r["choice_d"],
                    "user_answer": r["user_answer"],
                    "correct_answer": r["correct_answer"],
                    "result": r["result"],
                    "score": score,
                    "total": total,
                    "percent": f"{score / total * 100:.0f}%",
                }
            )

    print("📊 Detailed results saved to", file_path)


# ============================================================
# STEP 5: MAIN PROGRAM FLOW
# ============================================================


def main():
    print("🧠 QuizMe — AI Quiz Generator")
    print("=" * 35)

    notes = get_notes()
    if not notes:
        print("No notes entered!")
        return

    print("\nGenerating questions...")
    questions = generate_quiz(notes)

    if not questions:
        print("Could not generate quiz.")
        return

    score, total, results = run_quiz(questions)
    save_score(score, total, results)


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
    # Keeps the window open when packaged as an EXE
    input("\nPress Enter to exit...")
