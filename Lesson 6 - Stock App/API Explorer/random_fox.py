import requests
import csv

collected = []


def fetch_one():
    url = "https://randomfox.ca/floof/"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print("Could not fetch fox image")
            return
        data = response.json()
    except:
        print("Network error")
        return

    row = {
        "id": data.get("id"),
        "category": "Fox",
        "image": data.get("image"),
    }
    collected.append(row)
    print(f"\n{row["image"]}")
    print(f"Category: Fox")
    print(f"Added! ({len(collected)} images collected)")


def view_collected():
    if not collected:
        print("No images yet")
        return
    for i, j in enumerate(collected, 1):
        print(f"{i}. [{j["category"]}] {j["image"]}")


def save_and_quit():
    if not collected:
        print("Nothing to save")
        return

    filename = "images.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "category", "image"])
        writer.writeheader()
        writer.writerows(collected)
    print(f"Saved {len(collected)} images to {filename}")


def main():
    print("Random Fox Images Collector")
    print("=" * 30)

    while True:
        print("\n1. Get an image")
        print("2. View collected images")
        print("3. Save and quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            fetch_one()
        elif choice == "2":
            view_collected()
        elif choice == "3":
            save_and_quit()
            break
        else:
            print("Pick 1, 2, or 3")


if __name__ == "__main__":
    main()
