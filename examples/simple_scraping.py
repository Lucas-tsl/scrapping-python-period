"""
Version simple du scraping moderne - sans imports complexes
"""
import warnings
import requests
from bs4 import BeautifulSoup

# Supprimer les avertissements
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL 1.1.1+")

# Configuration
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_books_simple():
    """
    Scraping simple avec bonnes pratiques
    """
    print("🔍 Début du scraping de books.toscrape.com...")
    
    try:
        # Récupérer la page
        response = requests.get('https://books.toscrape.com/', headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        # Parser le HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraire les livres
        articles = soup.find_all("article", class_="product_pod")
        print(f"📚 {len(articles)} livres trouvés")
        
        books = []
        for article in articles[:5]:  # Limiter à 5 pour l'exemple
            title_elem = article.find("h3").find("a")
            price_elem = article.find("p", class_="price_color")
            
            book = {
                'title': title_elem.get('title', '') if title_elem else '',
                'price': price_elem.text.strip() if price_elem else '',
            }
            books.append(book)
            print(f"📖 {book['title']} - {book['price']}")
        
        print(f"✅ Scraping terminé - {len(books)} livres extraits")
        return books
        
    except requests.RequestException as e:
        print(f"❌ Erreur lors de la requête: {e}")
        return []
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return []

if __name__ == "__main__":
    scrape_books_simple()