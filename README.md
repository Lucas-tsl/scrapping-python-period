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

### Scripts d'apprentissage
```bash
python main.py                    # Parsing HTML local
python searchInfo-toscrapp.py     # Extraction simple
python all-book-info.py           # Scraping complet
```

### Exemples modernes
```bash
python examples/modern_scraping.py
```

### Tests
```bash
python -m pytest tests/ -v
```

## 🎯 Compétences Développées

- Navigation dans l'arbre DOM HTML
- Sélection d'éléments par classes CSS
- Extraction et nettoyage de données
- Gestion des requêtes HTTP avec headers
- Automatisation de navigateur web
- Tests unitaires et bonnes pratiques
- Structure de projet professionnel

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
