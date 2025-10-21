# Exemples de Scraping

Ce dossier contient différents exemples et scripts d'apprentissage.

## Scripts Recommandés (Nouveaux)

### `clean_scraping.py`
Script de scraping propre sans avertissements, idéal pour débuter.

### `modern_scraping.py` 
Script utilisant les utilitaires modulaires du projet.

### `simple_scraping.py`
Version simple avec gestion d'erreurs basique.

## Scripts Legacy (Apprentissage)

Ces scripts correspondent à votre parcours d'apprentissage initial :

- `legacy_main.py` - Premier script avec parsing HTML local
- `legacy_searchInfo-toscrapp.py` - Extraction d'informations
- `legacy_all-book-info.py` - Scraping complet
- `legacy_simulation.py` - Gestion des protections anti-bot
- `legacy_auto.py` - Automatisation avec Playwright
- `index.html` - Fichier HTML de test

## Utilisation

```bash
# Scripts recommandés
python3 examples/clean_scraping.py
python3 examples/modern_scraping.py

# Scripts d'apprentissage
python3 examples/legacy_main.py
python3 examples/legacy_searchInfo-toscrapp.py
```