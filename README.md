# Web Scraping avec Python

Projet d'apprentissage du web scraping utilisant BeautifulSoup4 et Playwright pour l'extraction de données web.

## Technologies

- **Python 3.9+**
- **BeautifulSoup4** - Parsing HTML statique
- **Requests** - Requêtes HTTP
- **Playwright** - Automatisation navigateur

## Installation

```bash
pip3 install requests beautifulsoup4 playwright
python3 -m playwright install
```

## Fonctionnalités

- Parsing de fichiers HTML locaux
- Extraction de données depuis des sites web
- Contournement des protections anti-bot
- Automatisation de navigateur pour contenu dynamique
- Gestion des erreurs SSL et urllib3

## Scripts Disponibles

| Script | Description |
|--------|-------------|
| `main.py` | Parsing HTML local de base |
| `searchInfo-toscrapp.py` | Extraction d'informations produits |
| `all-book-info.py` | Scraping complet avec détails |
| `simulation.py` | Gestion des protections web |
| `auto.py` | Automatisation avec Playwright |

## Utilisation

```bash
python3 <nom_du_script>.py
```

## Compétences Développées

- Navigation dans l'arbre DOM HTML
- Sélection d'éléments par classes CSS
- Extraction et nettoyage de données
- Gestion des requêtes HTTP avec headers
- Automatisation de navigateur web
- Résolution de problèmes de compatibilité SSL

---

*Projet éducatif - Lucas TSL*
