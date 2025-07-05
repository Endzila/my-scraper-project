import requests
from bs4 import BeautifulSoup
import re

url = "https://www.zlatabanka.com/investicni-zlato/zlate-investicni-slitky/zlaty-investicni-slitek-1-oz-argor-heraeus-9999-zlata-cihla-zlata-cihlicka-31-1-g.html"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Najdi první výskyt textu "Výkupní cena"
label = soup.find(string=lambda t: "Výkupní cena" in t)
if label:
    parent = label.find_parent()
    if parent:
        sibling = parent.find_next_sibling()
        if sibling:
            match = re.search(r"(\d{1,3}(?:\s?\d{3})*)\s*Kč", sibling.text)
            if match:
                price_str = match.group(1).replace("\xa0", "").replace(" ", "")
                print(f"Výkupní cena pro 1 oz Argor-Heraeus: {price_str} Kč")
            else:
                print("Výkupní cena nenalezena v sousedním elementu.")
        else:
            print("Sousední element nenalezen.")
    else:
        print("Rodičovský element nenalezen.")
else:
    print("Text 'Výkupní cena' nenalezen.")
