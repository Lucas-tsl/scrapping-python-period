import requests 
from bs4 import BeautifulSoup



def main():
    response = requests.get("https://books.toscrape.com/")
    soup = BeautifulSoup(response.text, "html.parser")

    #first_article = soup.find("article", class_="product_pod")
    #print(first_article.prettify())
    
    #first_article_name = soup.find("article", class_="product_pod").find("h3").find("a")["title"]
    #print(first_article_name)
    

    # all_articles = soup.find_all("article", class_="product_pod")
    # for article in all_articles:
    #     article_name = article.find("h3").find("a")["title"]
    #     print(article_name)

    # all_prices =soup.find_all("div", class_="product_price")
    # for price in all_prices: 
    #     article_price = price.find("p", class_="price_color")
    #     article_avaibility = price.find("p", class_="instock availability")
    #     print(article_price.text)
    #     print(article_avaibility.text)

    #Sous forme de liste par compréhension
    # articles = soup.find_all("article", class_="product_pod")
    # article_names = [article.find("h3").find("a")["title"] for article in articles]
    # print(article_names)

    # url = "https://books.toscrape.com/"

    # articles = soup.find_all("article", class_="product_pod")
    # article_urls = [url + article.find("h3").find("a")["href"] for article in articles]
    # print(article_urls)

    all_articles = soup.find_all("article", class_="product_pod")
    for article in all_articles:
        article_name = article.find("h3").find("a")["title"]
        print(article_name)

    nb_livres = len(all_articles)
    print(f"Nombre de livres : {nb_livres}") 

if __name__ == "__main__":
    main()

