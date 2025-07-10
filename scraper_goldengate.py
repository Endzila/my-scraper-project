import json
import os

os.chdir("/Users/mira/Documents/my-scraper-project/")

def scrape_goldengate():
    # Zde vložte reálný scraping kód pro zlato
    return "70032 Kč"

data = {}
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)

data["goldengate"] = scrape_goldengate()

with open("data.json", "w") as f:
    json.dump(data, f)
