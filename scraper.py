# Importy potřebné pro skript
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# --- FUNKCE PRO DETEKCI OPERACNIHO SYSTEMU ---
# Tato funkce vrací název operačního systému na základě hodnoty sys.platform.
def get_os_name():
    """
    Returns the name of the operating system.
    """
    platform_name = sys.platform
    if platform_name.startswith('win'):
        return 'Windows'
    elif platform_name == 'darwin':
        return 'macOS'
    elif platform_name.startswith('linux'):
        return 'Linux'
    else:
        return 'Unknown'

# --- NASTAVENI PROHLIZOCE NA ZAKLADE OS ---
print(f"Skript běží v prostředí: {get_os_name()}")

options = webdriver.ChromeOptions()
# Přidejte jakékoliv další volby, které potřebujete
# options.add_argument("--headless")  # Spustí prohlížeč bez grafického rozhraní
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--log-level=3") # Potlačí většinu výstupů z prohlížeče

# Spuštění Chrome bez parametru executable_path, protože Selenium 4.6+ to zvládá automaticky
try:
    if get_os_name() == 'macOS':
        # Pro macOS
        print("Spouštím prohlížeč Chrome na macOS...")
        driver = webdriver.Chrome(options=options)
    else:
        # Pro Windows a Linux
        print(f"Spouštím prohlížeč Chrome na {get_os_name()}...")
        driver = webdriver.Chrome(options=options)

except Exception as e:
    print(f"Chyba při spouštění prohlížeče: {e}")
    print("Ujistěte se, že máte nainstalovaný prohlížeč Google Chrome a že je ovladač v cestě (PATH).")
    sys.exit()

# --- WEB SCRAPING LOGIKA ---
# Zde začíná logika vašeho scraperu
try:
    # URL adresa stránky
    url = "https://www.alza.cz/mac-mini-m4"  # Zde vložte vaši cílovou URL

    print("Prohlížeč Chrome byl úspěšně spuštěn.")
    print("Čekám na načtení stránky a dynamického obsahu...")

    driver.get(url)

    # Čekání, aby se stihly načíst dynamické prvky (např. JavaScriptem)
    time.sleep(5) 

    # Zkuste zavřít banner s cookies, pokud existuje
    print("Zkouším zavřít banner s cookies...")
    try:
        # Příklad selektoru pro cookies banner, upravte podle potřeby
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cookies-consent-detail__body-buttons > div > a.btn.btn-accept"))
        )
        cookie_button.click()
        print("Banner s cookies byl zavřen.")
    except Exception:
        print("Banner s cookies se neobjevil, pokračuji.")
    
    # Najděte cenu
    # Hledá prvek s atributem 'data-price-amount' (Alza.cz)
    print("Hledám cenu pomocí nového, spolehlivého CSS selektoru...")
    try:
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-price-amount]"))
        )
        price_text = price_element.get_attribute("data-price-amount")
        print(f"Cena nalezena z atributu 'data-price-amount': {price_text}")
    except Exception:
        print("Chyba: Cena nebyla nalezena. Zkontrolujte selektor nebo se ujistěte, že je prvek na stránce.")

finally:
    print("Skript byl dokončen. Prohlížeč zůstane otevřený pro kontrolu.")
    print("Stiskněte Enter v terminálu pro zavření prohlížeče...")
    input()
    driver.quit()