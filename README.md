# 🕷️ Web Scraping avec Python - Guide d'Apprentissage

Bienvenue dans ce repository dédié à l'apprentissage du web scraping avec Python ! Ce projet vous guidera à travers les concepts fondamentaux et les techniques avancées pour extraire des données du web.

## 📋 Table des Matières

- [À propos](#à-propos)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Technologies Utilisées](#technologies-utilisées)
- [Structure du Projet](#structure-du-projet)
- [Premiers Pas](#premiers-pas)
- [Exemples](#exemples)
- [Bonnes Pratiques](#bonnes-pratiques)
- [Ressources](#ressources)
- [Contribuer](#contribuer)
- [Licence](#licence)

## 🎯 À propos

Ce projet est conçu pour vous apprendre le web scraping de manière progressive, en commençant par les bases et en explorant des techniques plus avancées. Vous apprendrez à :

- Faire des requêtes HTTP avec `requests`
- Parser du HTML avec `BeautifulSoup4`
- Extraire et structurer des données
- Gérer les erreurs et les exceptions
- Respecter les bonnes pratiques éthiques du scraping

## ⚙️ Prérequis

- Python 3.7 ou supérieur
- Connaissance de base en Python
- Compréhension basique du HTML
- Un éditeur de code (VS Code recommandé)

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/scrapping-python-period.git
cd scrapping-python-period
```

### 2. Créer un environnement virtuel (recommandé)

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou manuellement :

```bash
pip install requests beautifulsoup4
```

## 🛠️ Technologies Utilisées

- **[Python 3](https://www.python.org/)** - Langage de programmation
- **[Requests](https://requests.readthedocs.io/)** - Bibliothèque HTTP pour Python
- **[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)** - Bibliothèque de parsing HTML/XML
- **[lxml](https://lxml.de/)** (optionnel) - Parser XML/HTML plus rapide

## 📁 Structure du Projet

```
scrapping-python-period/
├── README.md
├── requirements.txt
├── .gitignore
├── exemples/
│   ├── 01_premier_scraper.py
│   ├── 02_extraction_donnees.py
│   ├── 03_gestion_erreurs.py
│   └── 04_scraper_avance.py
├── projets/
│   ├── scraper_citations/
│   ├── scraper_actualites/
│   └── scraper_produits/
└── data/
    └── resultats/
```

## 🎓 Premiers Pas

### Exemple de base

Voici un exemple simple pour commencer :

```python
import requests
from bs4 import BeautifulSoup

# Faire une requête HTTP
url = "https://example.com"
response = requests.get(url)

# Parser le HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Extraire des données
titre = soup.find('h1').text
print(f"Titre de la page : {titre}")
```

### Vérifier l'installation

```python
# test_installation.py
import requests
from bs4 import BeautifulSoup

print("✓ Requests version:", requests.__version__)
print("✓ BeautifulSoup installé avec succès!")
```

## 📚 Exemples

### 1. Scraper Simple
```python
# Extraire tous les liens d'une page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
```

### 2. Extraire des Données Structurées
```python
# Extraire des articles de blog
articles = soup.find_all('article', class_='post')
for article in articles:
    titre = article.find('h2').text
    auteur = article.find('span', class_='author').text
    print(f"{titre} par {auteur}")
```

### 3. Sauvegarder en CSV
```python
import csv

# Sauvegarder les données
with open('data/resultats.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Titre', 'Auteur', 'Date'])
    writer.writerow([titre, auteur, date])
```

## ✅ Bonnes Pratiques

### Respect des Règles

1. **Vérifier robots.txt** : Toujours consulter le fichier `robots.txt` du site
   ```
   https://example.com/robots.txt
   ```

2. **Respecter les délais** : Ajouter des pauses entre les requêtes
   ```python
   import time
   time.sleep(1)  # Pause de 1 seconde
   ```

3. **User-Agent** : Identifier votre bot
   ```python
   headers = {
       'User-Agent': 'Mon Bot de Scraping 1.0 (contact@email.com)'
   }
   response = requests.get(url, headers=headers)
   ```

### Gestion des Erreurs

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}")
```

### Considérations Légales et Éthiques

- ⚖️ Respectez les conditions d'utilisation des sites
- 🤝 Ne surchargez pas les serveurs
- 📜 Vérifiez la légalité du scraping dans votre juridiction
- 🔒 Ne scrapez pas de données personnelles sensibles
- 💡 Privilégiez les APIs officielles quand elles existent

## 📖 Ressources

### Documentation Officielle
- [Requests Documentation](https://requests.readthedocs.io/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Tutoriels
- [Real Python - Web Scraping](https://realpython.com/python-web-scraping-practical-introduction/)
- [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)

### Sites pour Pratiquer
- [Quotes to Scrape](http://quotes.toscrape.com/) - Site d'entraînement
- [Books to Scrape](http://books.toscrape.com/) - Catalogue de livres fictifs
- [Scrape This Site](https://www.scrapethissite.com/) - Exercices de scraping

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📧 Contact

Pour toute question ou suggestion :
- 📧 Email : votre.email@example.com
- 🐙 GitHub : [@votre-username](https://github.com/votre-username)

---

⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile !

**Happy Scraping! 🚀**
