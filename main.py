from bs4 import BeautifulSoup


def main():
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")
        # Chercher le premier h1, sans dépendre d'une classe spécifique
        title = soup.find('h1')
        if title:
            print(title.text)
        else:
            print("Aucun h1 trouvé")


if __name__ == "__main__":
    main()

