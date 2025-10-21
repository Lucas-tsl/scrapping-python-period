"""
Configuration centralisée pour les scripts de scraping
"""

# Headers communs pour simuler un navigateur
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

# URLs de test
TEST_URLS = {
    'books': 'https://books.toscrape.com/',
    'quotes': 'http://quotes.toscrape.com/',
    'httpbin': 'https://httpbin.org/',
}

# Configuration Playwright
PLAYWRIGHT_CONFIG = {
    'headless': False,
    'timeout': 30000,
    'viewport': {'width': 1920, 'height': 1080}
}

# Délais entre requêtes (respecter les serveurs)
REQUEST_DELAY = 1  # secondes