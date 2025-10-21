"""
Utilitaires communs pour les scripts de scraping
"""
import warnings
import time
import requests
from bs4 import BeautifulSoup
from config import DEFAULT_HEADERS, REQUEST_DELAY


def suppress_warnings():
    """Supprime les avertissements urllib3 et SSL"""
    warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
    warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL 1.1.1+")


def safe_get(url, headers=None, delay=REQUEST_DELAY):
    """
    Effectue une requête GET sécurisée avec gestion d'erreurs
    
    Args:
        url (str): URL à requêter
        headers (dict): Headers personnalisés
        delay (float): Délai avant la requête
        
    Returns:
        requests.Response: Réponse de la requête
    """
    if delay:
        time.sleep(delay)
    
    if headers is None:
        headers = DEFAULT_HEADERS
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Erreur lors de la requête vers {url}: {e}")
        return None


def parse_html(content):
    """
    Parse le contenu HTML avec BeautifulSoup
    
    Args:
        content (str): Contenu HTML à parser
        
    Returns:
        BeautifulSoup: Objet soup parsé
    """
    return BeautifulSoup(content, 'html.parser')


def extract_text_safe(element):
    """
    Extrait le texte d'un élément de manière sécurisée
    
    Args:
        element: Élément BeautifulSoup
        
    Returns:
        str: Texte extrait ou chaîne vide
    """
    return element.text.strip() if element else ""


def extract_attr_safe(element, attr):
    """
    Extrait un attribut d'un élément de manière sécurisée
    
    Args:
        element: Élément BeautifulSoup  
        attr (str): Nom de l'attribut
        
    Returns:
        str: Valeur de l'attribut ou chaîne vide
    """
    return element.get(attr, "") if element else ""