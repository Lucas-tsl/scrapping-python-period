# Web Scraping avec Python

Projet d'apprentissage du web scraping utilisant BeautifulSoup4 et Playwright pour l'extraction de données web.

## 🚀 Quick Start

```bash
git clone https://github.com/Lucas-tsl/scrapping-python-period.git
cd scrapping-python-period
./setup.sh  # Configuration automatique

# OU directement
python3 main.py  # Vue d'ensemble du projet
```

## Technologies

- **Python 3.9+**
- **BeautifulSoup4** - Parsing HTML statique
- **Requests** - Requêtes HTTP
- **Playwright** - Automatisation navigateur
- **Regex** - Recherche de motifs dans le texte

## 📁 Structure du Projet

```
scrapping-python-period/
├── src/                    # Code source organisé
├── examples/               # Exemples d'utilisation
├── tests/                  # Tests unitaires
├── docs/                   # Documentation détaillée
├── requirements.txt        # Dépendances Python
├── setup.sh               # Script de configuration
└── README.md              # Ce fichier
```

## 🛠️ Installation

### Méthode rapide
```bash
./setup.sh
```

### Méthode manuelle
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

Voir [docs/INSTALLATION.md](docs/INSTALLATION.md) pour plus de détails.

## 📖 Utilisation

### Scripts principaux
```bash
python main.py                    # Parsing HTML local
python src/airbnb-scrapper.py     # Scrapping Airbnb avec Playwright
```

### Scripts d'apprentissage (legacy)
```bash
python searchInfo-toscrapp.py     # Extraction simple
python all-book-info.py           # Scraping complet
```

### Exemples modernes
```bash
python examples/modern_scraping.py
python examples/clean_scraping.py
python examples/simple_scraping.py
```

### Tests
```bash
python -m pytest tests/ -v
```

## 🎯 Compétences Développées

- Navigation dans l'arbre DOM HTML
- Sélection d'éléments par classes CSS, ID, et attributs de test
- Extraction et nettoyage de données
- Gestion des requêtes HTTP avec headers
- Automatisation de navigateur web avec Playwright
- Interaction avec des éléments web (clic, remplissage de formulaires)
- Utilisation de regex pour la sélection d'éléments dynamiques
- Gestion des timeouts et attentes dans l'automatisation
- Tests unitaires et bonnes pratiques
- Structure de projet professionnel

## 🔧 Fonctionnalités

### Scrapper Airbnb (`src/airbnb-scrapper.py`)
- Automatisation complète d'une recherche Airbnb
- Gestion des cookies et consentements
- Recherche par localisation avec dates spécifiques
- Application de filtres avancés (type de logement, chambres, lits)
- Extraction des noms de propriétés
- Utilisation de différentes méthodes de sélection Playwright :
  - Sélection par rôle (`get_by_role`)
  - Sélection par ID (`locator`)
  - Sélection par texte (`get_by_text`)
  - Sélection par test-id (`get_by_test_id`)
  - Utilisation de regex pour les éléments dynamiques

## 📚 Documentation

- [Installation détaillée](docs/INSTALLATION.md)
- [Exemples d'utilisation](examples/)
- [Tests](tests/)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add some AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

---

*Projet éducatif - Lucas TSL*
