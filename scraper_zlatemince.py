import json
import os

os.chdir("/Users/mira/Documents/my-scraper-project/")

def scrape_zlatemince():
    # Zde vložte reálný scraping kód pro zlaté mince
    # Vraťte seznam 8 hodnot
    return [
        "69154 Kč", "69155 Kč", "69156 Kč", "69157 Kč",
        "69158 Kč", "69159 Kč", "69160 Kč", "69161 Kč"
    ]

data = {}
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)

data["zlatemince"] = scrape_zlatemince()

with open("data.json", "w") as f:
    json.dump(data, f)
