import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def pobierz_kursy_walut() -> list:
    """
    Pobiera kursy walut z API NBP.

    Returns:
        list: Lista kursów walut.
    """
    try:
        response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")
        data = response.json()[0]["rates"]
        return data
    except requests.exceptions.RequestException:
        messagebox.showerror("Błąd", "Nie udało się pobrać kursów walut.")
        return []


def pobierz_wartosc_zlota() -> float:
    """
    Pobiera wartość złota z API NBP.

    Returns:
        float: Cena złota.
    """
    try:
        response = requests.get("https://api.nbp.pl/api/cenyzlota/")
        data = response.json()[0]["cena"]
        return data
    except requests.exceptions.RequestException:
        messagebox.showerror("Błąd", "Nie udało się pobrać wartości złota.")
        return None


def przelicz_waluty(
    kursy: list, waluta_zrodlowa: str, waluta_docelowa: str, kwota: float
) -> float:
    """
    Przelicza kwotę z jednej waluty na inną.

    Args:
        kursy (list): Lista kursów walut.
        waluta_zrodlowa (str): Kod waluty źródłowej.
        waluta_docelowa (str): Kod waluty docelowej.
        kwota (float): Kwota do przeliczenia.

    Returns:
        float: Przeliczona kwota.
    """
    kurs_zrodlowy = None
    kurs_docelowy = None
    for waluta in kursy:
        if waluta["code"] == waluta_zrodlowa:
            kurs_zrodlowy = waluta["mid"]
        if waluta["code"] == waluta_docelowa:
            kurs_docelowy = waluta["mid"]
    if kurs_zrodlowy is None or kurs_docelowy is None:
        return None
    wynik = (kwota / kurs_zrodlowy) * kurs_docelowy
    return round(wynik, 2)


def oblicz() -> None:
    """
    Obsługuje logikę obliczeń po kliknięciu przycisku "Oblicz".
    """
    waluta_zrodlowa = combo_zrodlowa.get()
    waluta_docelowa = combo_docelowa.get()
    kwota_zrodlowa = float(entry_kwota.get())

    if waluta_zrodlowa == "PLN":
        wynik = przelicz_waluty(kursy, "USD", waluta_docelowa, kwota_zrodlowa) * 4.2
    elif waluta_docelowa == "PLN":
        wynik = przelicz_waluty(kursy, waluta_zrodlowa, "USD", kwota_zrodlowa) * 0.24
    else:
        wynik = przelicz_waluty(kursy, waluta_zrodlowa, waluta_docelowa, kwota_zrodlowa)

    if wynik is None:
        messagebox.showwarning("Ostrzeżenie", "Nie można przeliczyć walut.")
        return

    label_wynik.configure(text=str(wynik))


def aktualizuj_wartosc_zlota() -> None:
    """
    Aktualizuje wartość złota po kliknięciu przycisku.
    """
    wartosc_zlota = pobierz_wartosc_zlota()
    if wartosc_zlota:
        label_wartosc_zlota.configure(text=f"Aktualna wartość złota: {wartosc_zlota} PLN")
    else:
        messagebox.showwarning(
            "Ostrzeżenie", "Nie można pobrać aktualnej wartości złota. Wyświetlana jest poprzednia wartość."
        )


window = tk.Tk()
window.title("Przelicznik walut")

kursy = pobierz_kursy_walut()

waluty = [waluta["code"] for waluta in kursy]
waluty.append("PLN")

label_docelowa = tk.Label(window, text="Waluta źródłowa:")
label_docelowa.pack()

combo_docelowa = ttk.Combobox(window, values=waluty)
combo_docelowa.pack()

label_zrodlowa = tk.Label(window, text="Waluta docelowa:")
label_zrodlowa.pack()

combo_zrodlowa = ttk.Combobox(window, values=waluty)
combo_zrodlowa.pack()

label_kwota = tk.Label(window, text="Kwota:")
label_kwota.pack()

entry_kwota = tk.Entry(window)
entry_kwota.pack()

button_oblicz = tk.Button(window, text="Oblicz", command=oblicz)
button_oblicz.pack()

label_wynik = tk.Label(window, text="")
label_wynik.pack()

button_zakoncz = tk.Button(window, text="Zakończ", command=window.quit)
button_zakoncz.pack()

label_wartosc_zlota = tk.Label(window, text="")
label_wartosc_zlota.pack()

button_aktualizuj_zloto = tk.Button(window, text="Aktualizuj wartość złota", command=aktualizuj_wartosc_zlota)
button_aktualizuj_zloto.pack()

wartosc_zlota = pobierz_wartosc_zlota()
if wartosc_zlota:
    label_wartosc_zlota.configure(text=f"Aktualna wartość złota: {wartosc_zlota} PLN")
else:
    label_wartosc_zlota.configure(text="Nie można pobrać aktualnej wartości złota.")

window.mainloop()
