from pprint import pprint 
from bs4 import BeautifulSoup 
#from urlib.parse import urljoin
import re
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.airbnb.fr/")
        page.get_by_role("button", name="Accepter Tout").click()
        #BY id
        page.wait_for_timeout(1000)
        page.locator("#bigsearch-query-location-input").click()
        page.wait_for_timeout(1000)
        page.locator("#bigsearch-query-location-input").fill("les sables d'olonne")
        page.wait_for_timeout(1000)
        page.locator("#bigsearch-query-location-input").press("Enter")
        #BY role (button) + regex
        page.wait_for_timeout(1000)
        page.get_by_role("button", name=re.compile("25, Saturday, October 2025")).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name=re.compile("1, Saturday, November 2025")).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Rechercher").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Filtres").click()
        #BY text
        page.wait_for_timeout(1000)
        page.get_by_text("Logement entier").click()
        #BY test id
        page.wait_for_timeout(1000)
        for i in range(3):
            page.get_by_test_id("stepper-filter-item-min_bedrooms-stepper-increase-button").click()
        page.wait_for_timeout(1000)
        for i in range(5):
            page.get_by_test_id("stepper-filter-item-min_beds-stepper-increase-button").click()
        #BY role (link) + regex
        page.wait_for_timeout(1000)
        page.get_by_role("link", name=re.compile(r"Afficher \d+ logements")).click()
        page.wait_for_timeout(1000)
        page.pause()
        soup = BeautifulSoup(page.content(), 'html.parser')
        items = soup.find_all('div', attrs={'data-testid': 'listing-card-subtitle'})
        names = []
        for item in items: 
            try: 
                names.append(item.find('span').find("span").text)
            except:
                pass

        pprint(names)
        browser.close()

if __name__ == "__main__":
    main()