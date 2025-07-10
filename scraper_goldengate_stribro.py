import json
import os

os.chdir("/Users/mira/Documents/my-scraper-project/")

def scrape_goldengate_stribro():
    # Zde vložte reálný scraping kód pro stříbro
    return "25051 Kč"

data = {}
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)

data["goldengate_stribro"] = scrape_goldengate_stribro()

with open("data.json", "w") as f:
    json.dump(data, f)
