from src.explorer import crawl
import csv
import os
import random
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Wikipedia Topic Explorer")

    parser.add_argument(
        "--start",
        type=str,
        default=None,
        help="Starting Wikipedia article (URL or article name)"
    )
    parser.add_argument("--depth", type=int, default=None, help="Max crawl depth")
    parser.add_argument("--pages", type=int, default=None, help="Max pages to visit")
    parser.add_argument("--save", type=str, default="", help="CSV filename to save results")

    return parser.parse_args()

def normalize_start_url(user_input: str) -> str:
    """
    Accepts either:
    - Full Wikipedia URL
    - Article name (e.g. Albert_Einstein)
    """
    user_input = user_input.strip()

    if user_input.startswith("http"):
        return user_input

    article = user_input.replace(" ", "_")
    return f"https://en.wikipedia.org/wiki/{article}"

def main():
    args = parse_args()

    with open("randomWords.txt", mode="r", encoding="utf-8") as f:
        randomWords = [line.strip() for line in f]

    os.makedirs("data", exist_ok=True)

    # ---- START URL ----
    start_input = args.start or input(
        "Enter a Wikipedia article (URL or name, e.g. Albert_Einstein): "
    )

    start_url = normalize_start_url(start_input)

    # ---- DEPTH / PAGE LIMITS ----
    depth = args.depth if args.depth is not None else int(
        input("Enter crawl depth (e.g., 3): ")
    )
    pages = args.pages if args.pages is not None else int(
        input("Enter max pages (e.g., 15): ")
    )

    visited = crawl(start_url, depth, pages)

    print("\n-------------------------------")
    print("TOTAL SUBLINKS")
    print("-------------------------------")
    for url in visited:
        print(url)

    # ---- CSV SAVE ----
    if args.save:
        filename = args.save if args.save.endswith(".csv") else args.save + ".csv"
    else:
        decision = ""
        while decision.lower() not in ("y", "n"):
            decision = input("Would you like to save to a CSV? (Y/N): ")

        if decision.lower() == "y":
            filename = input("Enter CSV filename (blank = random): ")
            if not filename:
                filename = random.choice(randomWords).replace(" ", "_") + ".csv"
            elif not filename.endswith(".csv"):
                filename += ".csv"
        else:
            filename = ""

    if filename:
        filepath = os.path.join("data", filename)
        with open(filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["URL"])
            for url in sorted(visited):
                writer.writerow([url])

        print(f"\nSaved {len(visited)} links to {filepath}")


if __name__ == "__main__":
    main()
