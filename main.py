import requests 
from bs4 import BeautifulSoup

def main():
    response = reuqest.get('./index.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())


if __name__ == "__main__":
    main()

