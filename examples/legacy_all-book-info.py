import requests 
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("article", class_="product_pod")
article_urls = [url + article.find("h3").find("a")["href"] for article in articles]


for book_url in article_urls:
    response = requests.get(book_url)
    book_soup = BeautifulSoup(response.text, "html.parser")
    article_name = book_soup.find("h1").text
    article_price = book_soup.find("p", class_="price_color").text
    article_availability = book_soup.find("p", class_="instock availability")
    desc_div = book_soup.find("div", id="product_description")

    if desc_div:
        article_description = desc_div.find_next_sibling("p").text.strip()
    else:
        article_description = "No description available"
    print(f"nom du livre : {article_name}  - prix du livre : {article_price} - disponibilité : {article_availability.text}, description : {article_description}")



#float()
#regex
#strip