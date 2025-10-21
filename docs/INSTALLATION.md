# Guide d'Installation

## Prérequis

- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

### 1. Cloner le repository
```bash
git clone https://github.com/Lucas-tsl/scrapping-python-period.git
cd scrapping-python-period
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou
.venv\Scripts\activate     # Sur Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
python -m playwright install
```

## Utilisation

### Scripts de base
```bash
python main.py                    # Parsing HTML local
python searchInfo-toscrapp.py     # Extraction simple
python all-book-info.py           # Scraping complet
```

### Scripts avancés
```bash
python simulation.py              # Gestion anti-bot
python auto.py                    # Automatisation navigateur
```

## Troubleshooting

### Erreurs SSL/urllib3
Le script `simulation.py` gère automatiquement ces avertissements.

### Erreurs Playwright
Assurez-vous d'avoir installé les navigateurs :
```bash
python -m playwright install
```