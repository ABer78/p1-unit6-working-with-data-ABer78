import requests

API_KEY = "AIzaSyB5yFL-QJK3Kk_ov5CSabY6EPQykj8nhjk"

# ============================================================
# TODO: Construct the API endpoint URL piece by piece
# ============================================================
# Base URL for Google's Gemini API https://generativelanguage.googleapis.com
base_url = ""
# Model name (gemini-2.5-flash is fast and free-tier friendly)
model = ""
# Action (we want to generate content)
action = ""
# Combine everything and append your API key as a query parameter
# Hint: use an f-string: f"{base_url}/v1beta/models/{model}:{action}?key={API_KEY}"

url = ""  # <-- Build the URL here


def test_prompt(prompt_text):
    """
    Send a prompt to Gemini and print the response.
    """
    # TODO: Create the request body
    # It should be a dictionary with "contents" -> list containing a dict
    # with "parts" -> list containing a dict with "text" = prompt_text
    body = {}

    try:
        # TODO: Make the POST request (include a timeout of 30 seconds)
        response = None  # <-- Replace with requests.post(...)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"API error: {response.status_code}")
            print(response.text)
            return

        # TODO: Parse the JSON response and extract the text
        data = response.json()
        # The response structure: data["candidates"][0]["content"]["parts"][0]["text"]
        text = ""  # <-- Extract the text

        print("\n--- Gemini Response ---")
        print(text)
        print("------------------------\n")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("🧪 Testing Gemini API\n")

    # ============================================================
    # PHASE 1: Test a single prompt
    # ============================================================
    # TODO: Choose one of the prompts below, uncomment it, and test it.
    prompt1 = "Explain Python lists in one sentence."
    # prompt2 = "Give me three differences between a list and a tuple."
    # prompt3 = "Write a short code example showing how to create a dictionary."

    print(f"Testing single prompt: {prompt1}")
    test_prompt(prompt1)

    print("Done.")
