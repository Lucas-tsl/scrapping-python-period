#!/usr/bin/env python3
"""
Script principal du projet de scraping Python
"""
import warnings
import os

# Supprimer les avertissements
warnings.filterwarnings("ignore")
os.environ['PYTHONWARNINGS'] = 'ignore'

import sys
from pathlib import Path

# Ajouter src au path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from config import TEST_URLS
from utils import safe_get, parse_html

def main():
    """
    Fonction principale - Démonstration des capacités de scraping
    """
    print("🚀 Projet Web Scraping Python")
    print("=" * 50)
    
    print("\n📖 Exemples disponibles :")
    print("1. examples/clean_scraping.py - Scraping propre")
    print("2. examples/modern_scraping.py - Scraping avec utilitaires")
    print("3. examples/legacy_* - Scripts d'apprentissage originaux")
    
    print("\n🔧 Test rapide :")
    test_basic_scraping()
    
    print("\n💡 Pour utiliser :")
    print("  python3 examples/clean_scraping.py")
    print("  python3 examples/modern_scraping.py")
    print("  ./setup.sh  # Configuration complète")

def test_basic_scraping():
    """Test basique de scraping"""
    try:
        print("🔍 Test de connexion à books.toscrape.com...")
        response = safe_get(TEST_URLS['books'])
        if response:
            soup = parse_html(response.text)
            articles = soup.find_all("article", class_="product_pod")
            print(f"✅ Connexion réussie - {len(articles)} produits détectés")
        else:
            print("❌ Échec de connexion")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()