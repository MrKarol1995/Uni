import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import simplejson as json
import os

def pobierz_kursy_walut():
    """Funkcja pobierająca kurs walut ze strony NBP"""
    try:
        response = requests.get('https://api.nbp.pl/api/exchangerates/tables/A/')
        data = response.json()[0]['rates']
        with open('waluty.json', 'w') as plik:
            plik.write(json.dumps(data))
        return data
    except requests.exceptions.RequestException:
        if os.path.exists('waluty.json'):
            with open('waluty.json', 'r') as plik:
                data = json.load(plik)
            return data
        else:
            messagebox.showerror("Błąd", "Nie udało się pobrać kursów walut, a plik z danymi nie istnieje.")
            return None

def pobierz_wartosc_zlota():
    """Funkcja pobierająca wartość grama złota w PLN ze strony NBP"""
    try:
        response = requests.get('https://api.nbp.pl/api/cenyzlota/')
        data = response.json()[0]['cena']
        with open('zloto', 'w') as plik:
            plik.write(json.dumps(data))
        return data
    except requests.exceptions.RequestException:
        if os.path.exists('zloto'):
            with open('zloto', 'r') as plik:
                data = json.load(plik)
            return data
        else:
            messagebox.showerror("Błąd", "Nie udało się pobrać wartości złota.")
            return None

def przelicz_waluty(kursy, waluta_zrodlowa, waluta_docelowa, kwota):
    """funkcja przeliczająca waluty na inne waluty"""
    kurs_zrodlowy = None
    kurs_docelowy = None
    for waluta in kursy:
        if waluta['code'] == waluta_zrodlowa:
            kurs_zrodlowy = waluta['mid']
        if waluta['code'] == waluta_docelowa:
            kurs_docelowy = waluta['mid']
    if kurs_zrodlowy is None or kurs_docelowy is None:
        return None
    wynik = (kwota / kurs_zrodlowy) * kurs_docelowy
    return round(wynik, 5)

def oblicz():
    """funkcja licząca dane waluty za pomocą innej waluty i do listy walut"""
    waluta_zrodlowa = combo_zrodlowa.get()
    waluta_docelowa = combo_docelowa.get()
    kwota_zrodlowa = float(entry_kwota.get())
    wynik = przelicz_waluty(kursy, waluta_zrodlowa, waluta_docelowa, kwota_zrodlowa)
    if wynik is None:
        messagebox.showwarning("Ostrzeżenie", "Nie można przeliczyć walut.")
        return
    label_wynik.configure(text=str(wynik))

def przelicz_zloto(kwota, kursy, waluta_docelowa):
    """Funkcja przeliczająca złoto na inną walutę w zależności od ilości gramów"""
    with open("zloto", "r") as plik:
        ram = plik.read()
        gram = float(ram)
    kurs_docelowy = None
    for waluta in kursy:
        if waluta['code'] == waluta_docelowa:
            kurs_docelowy = waluta['mid']
            break
    if kurs_docelowy is None:
        return None
    wynik = kwota * gram * kurs_docelowy
    return round(wynik, 4)

def oblicz_zloto():
    """Funkcja obliczająca wartość złota w wybranej walucie"""
    waluta_docelowa = combo_zloto.get()
    gramy = float(entry_gramy.get())
    wynik = przelicz_zloto(gramy, kursy, waluta_docelowa)
    if wynik is None:
        messagebox.showwarning("Ostrzeżenie", "Nie można przeliczyć wartości złota.")
        return
    label_wynik_zloto.configure(text=str(wynik))



def aktualizuj_wartosc_zlota():
    """funkcja do pobierania na bierząco wartości złota"""
    wartosc_zlota = pobierz_wartosc_zlota()
    if wartosc_zlota:
        label_wartosc_zlota.configure(text=f"Aktualna wartość złota: {wartosc_zlota} w PLN")
    else:
        messagebox.showwarning("Ostrzeżenie", "Nie można pobrać aktualnej wartości złota. Wyświetlana jest poprzednia wartość.")




window = tk.Tk()
window.title("Przelicznik walut")

kursy = pobierz_kursy_walut()
kursy.append({'currency': 'złoty', 'code': 'PLN', 'mid': 1})
waluty = [waluta['code'] for waluta in kursy]

label_docelowa = tk.Label(window, text="Waluta źródłowa:")
label_docelowa.pack()

combo_docelowa = tk.ttk.Combobox(window, values=waluty)
combo_docelowa.pack()

label_zrodlowa = tk.Label(window, text="Waluta docelowa:")
label_zrodlowa.pack()

combo_zrodlowa = tk.ttk.Combobox(window, values=waluty)
combo_zrodlowa.pack()

label_kwota = tk.Label(window, text="Kwota:")
label_kwota.pack()

entry_kwota = tk.Entry(window)
entry_kwota.pack()

button_oblicz = tk.Button(window, text="Oblicz", command=oblicz)
button_oblicz.pack()

label_wynik = tk.Label(window, text="")
label_wynik.pack()

label_zloto = tk.Label(window, text="Przeliczanie kursu złota:")
label_zloto.pack()

combo_zloto = tk.ttk.Combobox(window, values=waluty)
combo_zloto.pack()

label_gramy = tk.Label(window, text="Gramy:")
label_gramy.pack()

entry_gramy = tk.Entry(window)
entry_gramy.pack()

button_oblicz_zloto = tk.Button(window, text="Oblicz", command=oblicz_zloto)
button_oblicz_zloto.pack()

label_wynik_zloto = tk.Label(window, text="")
label_wynik_zloto.pack()

label_wartosc_zlota = tk.Label(window, text="")
label_wartosc_zlota.pack()

button_aktualizuj_zloto = tk.Button(window, text="Aktualizuj wartość złota", command=aktualizuj_wartosc_zlota)
button_aktualizuj_zloto.pack()

wartosc_zlota = pobierz_wartosc_zlota()
if wartosc_zlota:
    label_wartosc_zlota.configure(text=f"Aktualna wartość złota: {wartosc_zlota} ")
else:
    label_wartosc_zlota.configure(text="Nie można pobrać aktualnej wartości złota.")

button_zakoncz = tk.Button(window, text="Zakończ", command=window.quit)
button_zakoncz.pack()
window.mainloop()
