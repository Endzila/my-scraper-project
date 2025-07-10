import subprocess
import json
from datetime import datetime
import os

# Nastavení pracovního adresáře na složku projektu
os.chdir("/Users/mira/Documents/my-scraper-project/")

# (Volitelné) Spuštění všech scrapperů – zakomentujte, pokud spouštíte ručně
subprocess.run(["/Users/mira/Documents/my-scraper-project/venv/bin/python", "scraper_goldengate.py"])
subprocess.run(["/Users/mira/Documents/my-scraper-project/venv/bin/python", "scraper_goldengate_stribro.py"])
subprocess.run(["/Users/mira/Documents/my-scraper-project/venv/bin/python", "scraper_zlatabanka.py"])
subprocess.run(["/Users/mira/Documents/my-scraper-project/venv/bin/python", "scraper_zlatemince.py"])

# Načtení hodnot
