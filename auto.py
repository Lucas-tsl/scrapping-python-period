#from pprint import pprint 
#from bs4 import BeautifulSoup 
#from urlib.parse import urljoin

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.pause()
        page.goto("http://locahost:5173/")
        browser.close()

if __name__ == "__main__":
    main()