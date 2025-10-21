"""
Tests unitaires pour les utilitaires de scraping
"""
import unittest
import sys
import os

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import extract_text_safe, extract_attr_safe, parse_html


class TestScrapingUtils(unittest.TestCase):
    
    def setUp(self):
        """Préparation des données de test"""
        self.html_content = """
        <html>
            <body>
                <h1 class="title">Test Title</h1>
                <p id="content">Test content</p>
                <a href="https://example.com">Test Link</a>
            </body>
        </html>
        """
        self.soup = parse_html(self.html_content)
    
    def test_parse_html(self):
        """Test du parsing HTML"""
        self.assertIsNotNone(self.soup)
        self.assertEqual(self.soup.find('h1').text, 'Test Title')
    
    def test_extract_text_safe(self):
        """Test d'extraction de texte sécurisée"""
        h1 = self.soup.find('h1')
        self.assertEqual(extract_text_safe(h1), 'Test Title')
        
        # Test avec élément inexistant
        self.assertEqual(extract_text_safe(None), '')
    
    def test_extract_attr_safe(self):
        """Test d'extraction d'attribut sécurisée"""
        link = self.soup.find('a')
        self.assertEqual(extract_attr_safe(link, 'href'), 'https://example.com')
        
        # Test avec attribut inexistant
        self.assertEqual(extract_attr_safe(link, 'nonexistent'), '')
        
        # Test avec élément inexistant
        self.assertEqual(extract_attr_safe(None, 'href'), '')


if __name__ == '__main__':
    unittest.main()