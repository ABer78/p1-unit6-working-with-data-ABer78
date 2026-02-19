# ============================================================
#  STOCK LOOKUP TOOL — Starter File
#  Unit 6, Lesson 6
# ============================================================

import requests, time


# ============================================================
# YOUR API KEY
# ============================================================
# TODO 1: Paste your Alpha Vantage API key between the quotes
#   Get your free key: https://www.alphavantage.co/support/#api-key
API_KEY = "Z19OTNUWQM2P3RH5"


# ============================================================
# DATA FUNCTION — This is what YOU will build!
# ============================================================


def get_stock_info(symbol):
    """
    Fetch stock data for a given ticker symbol from Alpha Vantage.

    Args:
        symbol (str): A stock ticker symbol like "AAPL" or "TSLA"

    Returns:
        dict: The "Global Quote" dictionary from Alpha Vantage, or None

    The returned dictionary has keys like:
        "01. symbol", "02. open", "03. high", "04. low",
        "05. price", "06. volume", "07. latest trading day",
        "08. previous close", "09. change", "10. change percent"
    """
    try:
        # TODO 2: Send a GET request to Alpha Vantage
        #   URL: "https://www.alphavantage.co/query"
        #   params dict should have:
        #       "function": "GLOBAL_QUOTE"
        #       "symbol":   symbol
        #       "apikey":   API_KEY
        #   Don't forget timeout=10!
        #
        #   Hint — this is the same pattern from Lesson 5:
        #       response = requests.get(url, params=params, timeout=10)
        url = "https://www.alphavantage.co/query"
        params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": API_KEY}
        response = requests.get(url, params=params, timeout=5)

        # TODO 3: Check the response and return the data
        #   - If status_code is 200:
        #       - Parse the JSON with response.json()
        #       - Get the "Global Quote" from the data using .get()
        #       - If the quote is NOT empty, return it
        #   - Otherwise, return None
        #
        #   Hint:
        #       data = response.json()
        #       quote = data.get("Global Quote", {})
        if response.status_code == 200:
            data = response.json()
            quote = data.get("Global Quote", {})
            if quote:
                return quote
        return None

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        print("Network error — check your internet connection.")
        return None


# ============================================================
# DISPLAY FUNCTIONS — Already built for you!
# ============================================================


def format_number(num_str):
    """Format a number string with commas (e.g., '48293847' → '48,293,847')."""
    try:
        return f"{int(num_str):,}"
    except (ValueError, TypeError):
        return num_str


def display_stock(quote, symbol):
    """
    Display formatted stock information.

    Args:
        quote (dict): The "Global Quote" dictionary from Alpha Vantage
        symbol (str): The ticker symbol (for display purposes)
    """
    print()
    print("─" * 40)
    print(f"  {symbol.upper()} — Stock Quote")
    print("─" * 40)
    print(f"  Price:        ${quote.get('05. price', 'N/A')}")
    print(f"  Open:         ${quote.get('02. open', 'N/A')}")
    print(f"  High:         ${quote.get('03. high', 'N/A')}")
    print(f"  Low:          ${quote.get('04. low', 'N/A')}")
    print(f"  Prev Close:   ${quote.get('08. previous close', 'N/A')}")
    print(f"  Volume:       {format_number(quote.get('06. volume', 'N/A'))}")
    print(
        f"  Change:       {quote.get('09. change', 'N/A')} ({quote.get('10. change percent', 'N/A')})"
    )
    print("─" * 40)


def display_comparison(quote1, symbol1, quote2, symbol2):
    """
    Display two stocks side by side for comparison.

    Args:
        quote1 (dict): First stock's Global Quote
        symbol1 (str): First stock's ticker symbol
        quote2 (dict): Second stock's Global Quote
        symbol2 (str): Second stock's ticker symbol
    """
    # Pre-format values for clean alignment
    price1 = quote1.get("05. price", "N/A")
    price2 = quote2.get("05. price", "N/A")
    open1 = quote1.get("02. open", "N/A")
    open2 = quote2.get("02. open", "N/A")
    high1 = quote1.get("03. high", "N/A")
    high2 = quote2.get("03. high", "N/A")
    low1 = quote1.get("04. low", "N/A")
    low2 = quote2.get("04. low", "N/A")
    close1 = quote1.get("08. previous close", "N/A")
    close2 = quote2.get("08. previous close", "N/A")
    vol1 = format_number(quote1.get("06. volume", "N/A"))
    vol2 = format_number(quote2.get("06. volume", "N/A"))
    chg1 = quote1.get("10. change percent", "N/A")
    chg2 = quote2.get("10. change percent", "N/A")

    print()
    print("═" * 52)
    print(f"  {'STOCK COMPARISON':^48}")
    print("═" * 52)
    print(f"  {'':15} {symbol1.upper():>15}  {symbol2.upper():>15}")
    print("─" * 52)
    print(f"  {'Price':15} {'$' + price1:>15}  {'$' + price2:>15}")
    print(f"  {'Open':15} {'$' + open1:>15}  {'$' + open2:>15}")
    print(f"  {'High':15} {'$' + high1:>15}  {'$' + high2:>15}")
    print(f"  {'Low':15} {'$' + low1:>15}  {'$' + low2:>15}")
    print(f"  {'Prev Close':15} {'$' + close1:>15}  {'$' + close2:>15}")
    print(f"  {'Volume':15} {vol1:>15}  {vol2:>15}")
    print(f"  {'Change':15} {chg1:>15}  {chg2:>15}")
    print("═" * 52)


# ============================================================
# MENU AND MAIN LOOP — Already built for you!
# ============================================================


def show_menu():
    """Display the main menu."""
    print()
    print("=" * 40)
    print("  📈 Stock Lookup Tool")
    print("=" * 40)
    print("  1. Look up a stock")
    print("  2. Compare two stocks")
    print("  3. Quit")
    print("=" * 40)


def lookup_stock():
    """Handle the single stock lookup flow."""
    symbol = input("\nEnter stock symbol: ").strip()
    if not symbol:
        print("No symbol entered.")
        return

    print(f"\nFetching data for {symbol.upper()}...")
    quote = get_stock_info(symbol)

    if quote:
        display_stock(quote, symbol)
    else:
        print(f"\nCould not find stock: {symbol.upper()}")
        print("Make sure you entered a valid ticker symbol (e.g., AAPL, TSLA)")


def compare_stocks():
    """Handle the stock comparison flow."""
    symbol1 = input("\nEnter first stock symbol: ").strip()
    symbol2 = input("Enter second stock symbol: ").strip()

    if not symbol1 or not symbol2:
        print("Please enter both stock symbols.")
        return

    print(f"\nFetching data for {symbol1.upper()} and {symbol2.upper()}...")

    quote1 = get_stock_info(symbol1)
    time.sleep(6)
    quote2 = get_stock_info(symbol2)
    print(quote1)
    print(quote2)

    if quote1 and quote2:
        display_comparison(quote1, symbol1, quote2, symbol2)
    elif not quote1:
        print(f"\nCould not find stock: {symbol1.upper()}")
    elif not quote2:
        print(f"\nCould not find stock: {symbol2.upper()}")


def main():
    """Main program loop."""
    print("\n🚀 Welcome to the Stock Lookup Tool!")
    print("Look up real-time stock data powered by Alpha Vantage.\n")

    if not API_KEY:
        print("⚠️  No API key set! Open this file and paste your key in TODO 1.")
        print("   Get a free key at: https://www.alphavantage.co/support/#api-key")
        return

    while True:
        show_menu()
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            lookup_stock()
        elif choice == "2":
            compare_stocks()
        elif choice == "3":
            print("\nThanks for using Stock Lookup Tool! 📈")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


# ============================================================
# RUN THE PROGRAM
# ============================================================
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        print()
        input("Press Enter to close...")
