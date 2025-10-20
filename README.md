# 🕷️ Web Scraping avec Python

Projet simple pour apprendre le web scraping avec Python, BeautifulSoup et Requests.

## 📦 Installation

```bash
pip3 install requests beautifulsoup4
```

## 🚀 Utilisation

```bash
python3 main.py
```

## 📁 Fichiers

- `main.py` - Script de scraping principal
- `index.html` - Fichier HTML d'exemple pour tester

## 💡 Exemple de base

```python
import requests
from bs4 import BeautifulSoup

# Récupérer une page web
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Parser le HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Extraire des données
titre = soup.find('title').text
print(titre)
```

## 📚 Ressources utiles

- [Documentation Requests](https://requests.readthedocs.io/)
- [Documentation BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Quotes to Scrape](http://quotes.toscrape.com/) - Site pour pratiquer

## ⚠️ Bonnes pratiques

- Vérifiez le fichier `robots.txt` des sites
- Respectez les délais entre les requêtes
- Ne surchargez pas les serveurs

---

Made by [@Lucas-tsl](https://github.com/Lucas-tsl)
