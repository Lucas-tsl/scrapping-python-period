#!/bin/bash

# Script de développement pour le projet de scraping

echo "🚀 Configuration de l'environnement de développement..."

# Créer l'environnement virtuel s'il n'existe pas
if [ ! -d ".venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv .venv
fi

# Activer l'environnement virtuel
echo "🔌 Activation de l'environnement virtuel..."
source .venv/bin/activate

# Installer les dépendances
echo "📥 Installation des dépendances..."
pip install -r requirements.txt

# Installer les navigateurs Playwright
echo "🌐 Installation des navigateurs Playwright..."
python -m playwright install

# Lancer les tests
echo "🧪 Lancement des tests..."
python -m pytest tests/ -v

echo "✅ Environnement prêt ! Vous pouvez maintenant développer."
echo "💡 Pour activer l'environnement : source .venv/bin/activate"