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
    availability = book_soup.find("p", class_="instock availability")
    print(f"{availability.text}")





    # all_articles = soup.find_all("article", class_="product_pod")
    # for article in all_articles:
    #     article_name = article.find("h3").find("a")["title"]
    #     print(article_name)

    # nb_livres = len(all_articles)
    # print(f"Nombre de livres : {nb_livres}")



