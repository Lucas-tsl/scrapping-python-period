"""
Version sans avertissements - suppression complète des warnings
"""
import warnings
import os

# Supprimer TOUS les avertissements urllib3 (méthode radicale)
warnings.filterwarnings("ignore")
os.environ['PYTHONWARNINGS'] = 'ignore'

import requests
from bs4 import BeautifulSoup

# Configuration
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_books_clean():
    """
    Scraping propre sans avertissements
    """
    print("🔍 Début du scraping de books.toscrape.com...")
    
    try:
        response = requests.get('https://books.toscrape.com/', headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all("article", class_="product_pod")
        
        print(f"📚 {len(articles)} livres trouvés")
        
        books = []
        for i, article in enumerate(articles[:5], 1):
            title_elem = article.find("h3").find("a")
            price_elem = article.find("p", class_="price_color")
            
            book = {
                'title': title_elem.get('title', '') if title_elem else '',
                'price': price_elem.text.strip() if price_elem else '',
            }
            books.append(book)
            print(f"📖 #{i} {book['title']} - {book['price']}")
        
        print(f"✅ Scraping terminé - {len(books)} livres extraits")
        return books
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return []

if __name__ == "__main__":
    scrape_books_clean()