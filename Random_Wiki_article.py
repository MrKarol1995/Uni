import requests
from bs4 import BeautifulSoup
import webbrowser
while True:
    # losuj losowy artykuł z Wikipedii
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    print(response.status_code)
    so = BeautifulSoup(response.content, "html.parser")
    title = so.find("h1", {"class": "firstHeading"}).text
    url = response.url

    # pytaj użytkownika, czy otworzyć artykuł
    print(f"Losowy artykuł: {title}")
    response = input("Czy chcesz otworzyć ten artykuł? (Tak/Nie): ")
    if response.lower() == "tak":
        # otwórz artykuł w przeglądarce
        webbrowser.open_new_tab(url)
        break
