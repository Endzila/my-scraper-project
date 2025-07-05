import requests
from bs4 import BeautifulSoup
import re

url = "https://zlatemince.cz/argor-heraeus-sa-1-oz-investicni-zlaty-slitek-investice-0000482"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

labels = soup.find_all(string=lambda t: "Výkupní cena" in t)

printed = False
for label in labels:
    parent = label.find_parent()
    sibling = parent.find_next_sibling() if parent else None
    price = None
    # Nejprve zkus najít cenu v siblingu
    if sibling:
        match = re.search(r"(\d{1,3}(?:\s?\d{3})*),\d{2}\s*Kč", sibling.text)
        if match:
            price = match.group(1).replace("\xa0", "").replace(" ", "")
    # Pokud není v siblingu, zkus v rodiči
    if not price and parent:
        match_parent = re.search(r"(\d{1,3}(?:\s?\d{3})*),\d{2}\s*Kč", parent.text)
        if match_parent:
            price = match_parent.group(1).replace("\xa0", "").replace(" ", "")
    if price and not printed:
        print(f"Výkupní cena: {price} Kč")
        printed = True
        break

if not printed:
    print("Výkupní cena nebyla nalezena.")
