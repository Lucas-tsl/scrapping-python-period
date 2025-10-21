# Liste de parfums disponibles
parfums = [
    {"nom": "Parfum A", "sillage": "chaleureux", "accord": "boise"},
    {"nom": "Parfum B", "sillage": "doux", "accord": "boise"},
    {"nom": "Parfum C", "sillage": "rafraichissant", "accord": "gourmand"},
    {"nom": "Parfum D", "sillage": "mysterieux", "accord": "boise"},
    {"nom": "Parfum E", "sillage": "seduisant", "accord": "gourmand"},
    {"nom": "Parfum F", "sillage": "solaire", "accord": "boise"},
    {"nom": "Parfum G", "sillage": "reconfortant", "accord": "gourmand"},
]

def recommander_parfum():
    print("Bienvenue sur le bot de recommandation de parfum! 🥰")
    
    # Demander le sillage
    sillage = input("Choisissez un sillage parmi : doux, chaleureux, rafraichissant, mysterieux, seduisant, solaire, reconfortant : ").lower()
    while sillage not in [p["sillage"] for p in parfums]:
        sillage = input("Veuillez choisir un sillage valide : ").lower()
    
    # Demander l'accord
    accord = input("Choisissez un accord parmi : boise, gourmand : ").lower()
    while accord not in [p["accord"] for p in parfums]:
        accord = input("Veuillez choisir un accord valide : ").lower()

    # Filtrer les parfums
    suggestions = [p["nom"] for p in parfums if p["sillage"] == sillage and p["accord"] == accord]

    # Afficher les résultats
    if suggestions:
        print("\nVoici les parfums qui correspondent à votre choix :")
        for parfum in suggestions:
            print(f" - {parfum}")
    else:
        print("\nDésolé, aucun parfum ne correspond exactement à votre choix.")

# Lancer le bot
recommander_parfum()
