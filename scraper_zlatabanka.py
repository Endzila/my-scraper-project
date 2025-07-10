import json
import os

os.chdir("/Users/mira/Documents/my-scraper-project/")

def scrape_zlatabanka():
    # Zde vložte reálný scraping kód pro zlatabanku
    # Pokud chcete dvě hodnoty, vraťte seznam dvou hodnot, např.:
    return ["67791 Kč", "67792 Kč"]

data = {}
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)

data["zlatabanka"] = scrape_zlatabanka()

with open("data.json", "w") as f:
    json.dump(data, f)
