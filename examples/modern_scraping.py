"""
Exemple moderne de scraping avec gestion d'erreurs et bonnes pratiques
"""
import warnings
# Supprimer les avertissements dès le début
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL 1.1.1+")

import sys
import os

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import suppress_warnings, safe_get, parse_html, extract_text_safe, extract_attr_safe
from config import TEST_URLS


def scrape_books_modern():
    """
    Exemple de scraping moderne avec gestion d'erreurs
    """
    suppress_warnings()
    
    print("🔍 Début du scraping de books.toscrape.com...")
    
    # Récupérer la page
    response = safe_get(TEST_URLS['books'])
    if not response:
        print("❌ Impossible de récupérer la page")
        return
    
    # Parser le HTML
    soup = parse_html(response.text)
    
    # Extraire les livres
    books = []
    articles = soup.find_all("article", class_="product_pod")
    
    print(f"📚 {len(articles)} livres trouvés")
    
    for article in articles[:5]:  # Limiter à 5 pour l'exemple
        book = {
            'title': extract_attr_safe(article.find("h3").find("a"), 'title'),
            'price': extract_text_safe(article.find("p", class_="price_color")),
            'availability': extract_text_safe(article.find("p", class_="instock availability")),
            'url': extract_attr_safe(article.find("h3").find("a"), 'href')
        }
        books.append(book)
        
        print(f"📖 {book['title']} - {book['price']}")
    
    print(f"✅ Scraping terminé - {len(books)} livres extraits")
    return books


if __name__ == "__main__":
    scrape_books_modern()