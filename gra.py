import pygame
import random
import time
from rembg import remove
from PIL import Image

# Rozpoczęcie funkcji pygame
pygame.init()

# Rozpoczęcie modułu muzycznego
pygame.mixer.init()

# Wczytanie dźwięków
explosion_dzwiek = pygame.mixer.Sound("expload.wav")
explosion_dzwiek2 = pygame.mixer.Sound("Explosion7.wav")
explosion_dzwiek3 = pygame.mixer.Sound("demo.wav")

# Ustawienia okna gry
szerokosc_okna = 1150
wysokosc_okna = 700
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("Gra kosmiczna")

# Statystyki gracza
gracz_szerokosc = 45
gracz_wysokosc = 50
gracz_x = (szerokosc_okna - gracz_szerokosc) // 2
gracz_y = wysokosc_okna - gracz_wysokosc - 10
gracz_ruch = 1.8

# Statystyki komet
kometa_szerokosc = 45
kometa_wysokosc = 40
liczba_komet = 18
komety = []
for _ in range(liczba_komet):
    kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
    kometa_y = random.randint(-500, -50)
    kometa_ruch = random.uniform(1, 1.8)
    komety.append((kometa_x, kometa_y, kometa_ruch))

# Statystyki pocisku
pocisk_szerokosc = 15
pocisk_wysokosc = 20
pocisk_x = 0
pocisk_y = gracz_y
pocisk_ruch = 5
pocisk_aktywny = False

# Statystyki pocisków podwójnych
pocisk_x1 = 0
pocisk_y1 = gracz_y
pocisk_x2 = 0
pocisk_y2 = gracz_y
pocisk_aktywny1 = False
pocisk_aktywny2 = False

# Obcięcie tła z grafik
input_path = 'kometa2.png'
output_path = 'kometa5.png'
input1 = Image.open(input_path)
output = remove(input1)
output.save(output_path)
input_path2 = 'statek5.jpg'
output_path2 = 'nowy.png'
input2 = Image.open(input_path2)
output2 = remove(input2)
output2.save(output_path2)

# Grafika tła
tlo_obraz = pygame.image.load("tlo.jpg")
tlo_obraz = pygame.transform.scale(tlo_obraz, (szerokosc_okna, wysokosc_okna))

# Grafika dla spadających komet
kometa_obraz = pygame.image.load("kometa5.png")
kometa_obraz = pygame.transform.scale(kometa_obraz, (kometa_szerokosc, kometa_wysokosc))

# Grafika dla pocisku
pocisk_obraz = pygame.image.load("pocisk.png")
pocisk_obraz = pygame.transform.scale(pocisk_obraz, (pocisk_szerokosc, pocisk_wysokosc))

# Grafika tła
tlo = pygame.image.load("space.jpg")
tlo = pygame.transform.scale(tlo, (szerokosc_okna, wysokosc_okna))

# Grafiki statków
statki_obrazy = [
    pygame.image.load("statek.png"),
    pygame.image.load("statek2.png"),
    pygame.image.load("nowy.png")
]
statki_obrazy = [pygame.transform.scale(statek_obraz, (gracz_szerokosc, gracz_wysokosc)) for statek_obraz in statki_obrazy]

# Czcionka
czcionka = pygame.font.SysFont("ComicSans", 35)

# zmienne
licznik_strzalow = 10
poziom_trudnosci = 1
wynikii = []
suma = 0
punkty = 0
aktualny_statek = 0
zycie = 3
paliwo = 0
bialy = (193, 156, 242)
inny = (242, 242, 242)

def zapisz(wynikk):
    """Funkcja do zapisu wyników do pliku"""
    with open('scores.txt', 'a') as file:
        file.write(str(wynikk) + '\n')

def najlepszy():
    """Funkcja do odczytania 3 najlepszych wyników z pliku"""
    lista1 = []
    with open('scores.txt', 'r') as file:
        for line in file:
            lista1.append(int(line.strip()))
    top_ = sorted(lista1, reverse=True)[:3]
    return top_
# Funkcja kończenia
def wyjdz_z_programu():
    """Funkcja do wyjścia z gry"""
    pygame.quit()
    quit()

# Funkcja wyświetlająca ekran początkowy
def ekran_poczatkowy():
    """Funkcja do wyświetlania menu początkowego"""
    global aktualny_statek, poziom_trudnosci
    while True:
        najlepszy()
        okno.blit(tlo, (0, 0))
        tekst_naglowek = czcionka.render("Gra kosmiczna", True, bialy)
        tekst_instrukcje = czcionka.render("Naciśnij SPACJĘ, aby rozpocząć", True, bialy)
        tekst_poziom = czcionka.render("Poziom trudności: " + str(poziom_trudnosci), True, bialy)
        tekst_exit = czcionka.render("Wyłącz grę, naciśnij 0: ", True, bialy)
        teskt_zasady = czcionka.render("Zasady Gry, naciśnij 2: ", True, inny)
        tabela = czcionka.render("Tabela wyników: " + str(najlepszy()), True, bialy)
        explosion_dzwiek3.play()

        okno.blit(tekst_naglowek, (szerokosc_okna // 2 - tekst_naglowek.get_width() // 2, wysokosc_okna // 2 - 300))
        okno.blit(tekst_instrukcje, (szerokosc_okna // 2 - tekst_instrukcje.get_width() // 2, wysokosc_okna // 2 - 200))
        okno.blit(tekst_poziom, (szerokosc_okna // 2 - tekst_poziom.get_width() // 2, wysokosc_okna // 2 + 100))
        okno.blit(statki_obrazy[aktualny_statek], (szerokosc_okna // 2 - gracz_szerokosc // 2, wysokosc_okna // 2 + 50))
        okno.blit(tekst_exit, (szerokosc_okna // 2 - tekst_exit.get_width() // 2, wysokosc_okna // 2 + 212))
        okno.blit(teskt_zasady, (szerokosc_okna // 2 - teskt_zasady.get_width() // 2, wysokosc_okna // 2 + 150))
        okno.blit(tabela, (szerokosc_okna // 2 - tabela.get_width() // 2, wysokosc_okna // 2 + 280))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wyjdz_z_programu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return poziom_trudnosci
                if event.key == pygame.K_RIGHT:
                    aktualny_statek = (aktualny_statek + 1) % len(statki_obrazy)
                if event.key == pygame.K_LEFT:
                    aktualny_statek = (aktualny_statek - 1) % len(statki_obrazy)
                if event.key == pygame.K_UP:
                    poziom_trudnosci += 1
                if event.key == pygame.K_DOWN:
                    poziom_trudnosci -= 1
                if event.key == pygame.K_2:
                    instrukcje()
                if event.key == pygame.K_0:
                    wyjdz_z_programu()
                if event.key == pygame.K_SPACE:
                    return  # Zwracamy False w przypadku przegranej gry
                if event.key == pygame.K_n:
                    return False  # Zwracamy False w przypadku powrotu z ekranu końca gry

                poziom_trudnosci = max(1, min(poziom_trudnosci, 10))

def instrukcje():
    """Funkcja do Instrukcji obsługi gry"""
    while True:
        okno.blit(tlo, (0, 0))
        tekst_naglowek = czcionka.render("Gra polega na niszczniu komet i nie daniu się zniszczyć. ", True, bialy)
        tekst1 = czcionka.render(" W menu możesz wybrać statek i poziom trudności,", True, bialy)
        tekst2 = czcionka.render("odpowiednio strzałkami prawo lewo, góra dół, a strzela się spacją.", True, bialy)
        tekst_powrot = czcionka.render("Podwót do menu glownego, naciśnij 7: ", True, inny)
        explosion_dzwiek3.play()

        okno.blit(tekst_naglowek, (szerokosc_okna // 2 - tekst_naglowek.get_width() // 2, wysokosc_okna // 2 - 300))
        okno.blit(tekst1, (szerokosc_okna // 2 - tekst_naglowek.get_width() // 2, wysokosc_okna // 2 - 250))
        okno.blit(tekst2, (szerokosc_okna // tekst_naglowek.get_width() + 6 // 2, wysokosc_okna // 2 - 200))
        okno.blit(tekst_powrot, (szerokosc_okna // 2 - tekst_powrot.get_width() // 2, wysokosc_okna // 2 - 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wyjdz_z_programu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_7:
                    return False
                if event.key == pygame.K_0:
                    wyjdz_z_programu()

# Funkcja wyświetlająca ekran końca gry
def ekran_konca_gry():
    """Funkcja do ekranu końca gry"""
    while True:
        okno.blit(tlo, (0, 0))
        time.sleep(1)
        explosion_dzwiek3.play()
        tekst_koniec = czcionka.render("GAME OVER!", True, bialy)
        tekst_wynik = czcionka.render("Twój wynik: " + str(punkty), True, bialy)
        tekst_kontynuuj = czcionka.render("Czy chcesz zagrać ponownie? (T/N)", True, bialy)
        autor = czcionka.render("Program przygotwany przez: Karola Cieślika Ambitnego studenta", True, inny)
        autor2 = czcionka.render("MST na Pwr,który nieustannie poszukuje nowych wyzwań.", True, inny)

        okno.blit(autor, (szerokosc_okna // 2 - autor.get_width() // 2, wysokosc_okna // 2 + 200))
        okno.blit(autor2, (szerokosc_okna // 2 - tekst_kontynuuj.get_width() + 50 // 2, wysokosc_okna // 2 + 280))
        okno.blit(tekst_koniec, (szerokosc_okna // 2 - tekst_koniec.get_width() // 2, wysokosc_okna // 2 - 100))
        okno.blit(tekst_wynik, (szerokosc_okna // 2 - tekst_wynik.get_width() // 2, wysokosc_okna // 2 - 50))
        okno.blit(tekst_kontynuuj, (szerokosc_okna // 2 - tekst_kontynuuj.get_width() // 2, wysokosc_okna // 2+50))
        okno.blit(tekst_kontynuuj, (szerokosc_okna // 2 - tekst_kontynuuj.get_width() // 2, wysokosc_okna // 2 + 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wyjdz_z_programu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return True
                if event.key == pygame.K_n:
                    return False
def brak():
    """Funkcja warunkowego końca"""
    while True:
        okno.blit(tlo, (0, 0))
        time.sleep(1)
        explosion_dzwiek3.play()
        tekst_koniec = czcionka.render("Straciłeś życie!", True, bialy)
        tekst_wynik = czcionka.render("Twój wynik: " + str(punkty), True, bialy)
        tekst_kontynuuj = czcionka.render("Aby kontynuować lub przerwać naciśnij odpowiednio (T/N)", True, bialy)

        okno.blit(tekst_koniec, (szerokosc_okna // 2 - tekst_koniec.get_width() // 2, wysokosc_okna // 2 - 100))
        okno.blit(tekst_wynik, (szerokosc_okna // 2 - tekst_wynik.get_width() // 2, wysokosc_okna // 2 - 50))
        okno.blit(tekst_kontynuuj, (szerokosc_okna // 2 - tekst_kontynuuj.get_width() // 2, wysokosc_okna // 2+50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wyjdz_z_programu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return True
                if event.key == pygame.K_n:
                    return False


# Główna pętla gry
ekran_poczatkowy()
gra_trwa = True

# Licznik czasu
czas_poczatkowy = time.time()

while True:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wyjdz_z_programu()

        # Strzelanie pociskiem po wciśnięciu spacji
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not pocisk_aktywny:
                    pocisk_x = gracz_x + gracz_szerokosc // 2 - pocisk_szerokosc // 2
                    pocisk_y = gracz_y
                    pocisk_aktywny = True
                    licznik_strzalow += 1
                    if punkty >= 50 and licznik_strzalow % 2 == 0:
                        pocisk_x1 = pocisk_x - 20
                        pocisk_x2 = pocisk_x + pocisk_szerokosc
                        pocisk_y1 = pocisk_y
                        pocisk_y2 = pocisk_y
                        pocisk_aktywny1 = True
                        pocisk_aktywny2 = True

        # Poruszanie graczem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gracz_x > 0:
        if paliwo < 35:
            gracz_x -= gracz_ruch / 2
        else:
            gracz_x -= gracz_ruch
    if keys[pygame.K_RIGHT] and gracz_x < szerokosc_okna - gracz_szerokosc:
        if paliwo < 35:
            gracz_x += gracz_ruch / 2
        else:
            gracz_x += gracz_ruch

    # Poruszanie komet
    for i in range(liczba_komet):
        kometa_x, kometa_y, kometa_ruch = komety[i]
        kometa_y += (kometa_ruch / 2) + (poziom_trudnosci * 0.1)
        if kometa_y > wysokosc_okna:
            kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
            kometa_y = random.randint(-500, -50)
            kometa_ruch = random.uniform(0.8, 2) + (poziom_trudnosci * 0.1)
        komety[i] = (kometa_x, kometa_y, kometa_ruch)
        nowy_czas = time.time()

        # Sprawdzanie kolizji pocisku z kometa
        if pocisk_aktywny and pocisk_y < kometa_y + kometa_wysokosc and pocisk_y + pocisk_wysokosc > kometa_y:
            if pocisk_x < kometa_x + kometa_szerokosc and pocisk_x + pocisk_szerokosc > kometa_x:
                pocisk_aktywny = False
                punkty += 1
                if punkty >= 25:
                    punkty += 2
                kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
                kometa_y = random.randint(-500, -50)
                kometa_ruch = random.uniform(0.6, 1.5)+0.1*int(nowy_czas)
                komety[i] = (kometa_x, kometa_y, kometa_ruch)
                explosion_dzwiek.play()  # Odtwarzanie dźwięku eksplozji

        # Sprawdzanie kolizji statku gracza z kometa
        if gracz_y < kometa_y + kometa_wysokosc and gracz_y + gracz_wysokosc > kometa_y:
            if gracz_x < kometa_x + kometa_szerokosc and gracz_x + gracz_szerokosc > kometa_x:
                explosion_dzwiek2.play()  # Odtwarzanie dźwięku eksplozji
                zycie -= 1
                if brak():
                    # Zerowanie statystyk
                    gracz_x = (szerokosc_okna - gracz_szerokosc) // 2
                    gracz_y = wysokosc_okna - gracz_wysokosc - 10
                    komety = []
                    for _ in range(liczba_komet):
                        kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
                        kometa_y = random.randint(-500, -50)
                        kometa_ruch = random.uniform(0.1, 1)
                        komety.append((kometa_x, kometa_y, kometa_ruch))
                    czas_poczatkowy = time.time()
                    licznik_strzalow = 0
                    zapisz(punkty)
                    top = najlepszy()
                    punkty = 0
                    continue
                else:
                    wyjdz_z_programu()

        # Sprawdzanie kolizji pocisków podwójnych z kometa
        if pocisk_aktywny1 and pocisk_y1 < kometa_y + kometa_wysokosc and pocisk_y1 + pocisk_wysokosc > kometa_y:
            if pocisk_x1 < kometa_x + kometa_szerokosc and pocisk_x1 + pocisk_szerokosc > kometa_x:
                pocisk_aktywny1 = False
                punkty += 1
                if punkty >= 25:
                    punkty += 2
                kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
                kometa_y = random.randint(-500, -50)
                kometa_ruch = random.uniform(0.8, 2)
                komety[i] = (kometa_x, kometa_y, kometa_ruch)
        if pocisk_aktywny2 and pocisk_y2 < kometa_y + kometa_wysokosc and pocisk_y2 + pocisk_wysokosc > kometa_y:
            if pocisk_x2 < kometa_x + kometa_szerokosc and pocisk_x2 + pocisk_szerokosc > kometa_x:
                pocisk_aktywny2 = False
                punkty += 1
                if punkty >= 25:
                    punkty += 2
                kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
                kometa_y = random.randint(-500, -50)
                kometa_ruch = random.uniform(0.8, 2)+0.2*int(nowy_czas)
                komety[i] = (kometa_x, kometa_y, kometa_ruch)

    # Poruszanie pociskiem
    if pocisk_aktywny:
        pocisk_y -= pocisk_ruch
        if pocisk_y < 0:
            pocisk_aktywny = False
    if pocisk_aktywny1:
        pocisk_y1 -= pocisk_ruch
        if pocisk_y1 < 0:
            pocisk_aktywny1 = False
    if pocisk_aktywny2:
        pocisk_y2 -= pocisk_ruch
        if pocisk_y2 < 0:
            pocisk_aktywny2 = False

    # Wyświetlanie obiektów na ekranie
    okno.blit(tlo_obraz, (0, 0))
    okno.blit(statki_obrazy[aktualny_statek], (gracz_x, gracz_y))
    for i in range(liczba_komet):
        okno.blit(kometa_obraz, (komety[i][0], komety[i][1]))
    if pocisk_aktywny:
        okno.blit(pocisk_obraz, (pocisk_x, pocisk_y))
    if pocisk_aktywny1:
        okno.blit(pocisk_obraz, (pocisk_x1, pocisk_y1))
    if pocisk_aktywny2:
        okno.blit(pocisk_obraz, (pocisk_x2, pocisk_y2))

    # Wyświetlanie punktów
    tekst_punkty = czcionka.render("Punkty: " + str(punkty), True, bialy)
    okno.blit(tekst_punkty, (10, 10))

    # Wyświetlanie liczników
    czas_gry = int(time.time() - czas_poczatkowy)
    czas_napis = czcionka.render("Czas: " + str(czas_gry) + "s", True, bialy)
    okno.blit(czas_napis, (10, 50))

    # Wyświetlanie stanu paliwa
    paliwo = round(int(50-czas_gry*0.9) + punkty / 3, 2)
    paliwo_napis = czcionka.render("Paliwo: " + str(paliwo), True, bialy)
    okno.blit(paliwo_napis, (880, 10))

    # zycie
    zycie_napis = czcionka.render("Licznik żyć: " + str(zycie), True, bialy)
    okno.blit(zycie_napis, (880, 50))

# Aktualizacja ekranu
    pygame.display.update()

    # Sprawdzenie warunku końca gry (czas)
    if czas_gry >= 100 or paliwo <= 30:
        if ekran_konca_gry():
            # Zerowanie statystyk
            suma += punkty
            gracz_x = (szerokosc_okna - gracz_szerokosc) // 2
            gracz_y = wysokosc_okna - gracz_wysokosc - 10
            komety = []
            for _ in range(liczba_komet):
                kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
                kometa_y = random.randint(-500, -50)
                kometa_ruch = random.uniform(0.8, 2)
                komety.append((kometa_x, kometa_y, kometa_ruch))
                czas_poczatkowy = time.time()
            licznik_strzalow = 0
            zapisz(punkty)
            top = najlepszy()
            punkty = 0
            continue
        else:
            wyjdz_z_programu()
    if zycie <= 0:
        ekran_konca_gry()
        # Zerowanie statystyk
        suma += punkty
        gracz_x = (szerokosc_okna - gracz_szerokosc) // 2
        gracz_y = wysokosc_okna - gracz_wysokosc - 10
        komety = []
        for _ in range(liczba_komet):
            kometa_x = random.randint(0, szerokosc_okna - kometa_szerokosc)
            kometa_y = random.randint(-500, -50)
            kometa_ruch = random.uniform(0.8, 2)
            komety.append((kometa_x, kometa_y, kometa_ruch))
            czas_poczatkowy = time.time()
        licznik_strzalow = 0
        zapisz(punkty)
        top = najlepszy()
        punkty = 0
        ekran_poczatkowy()
        zapisz(punkty)
        zycie = 3
