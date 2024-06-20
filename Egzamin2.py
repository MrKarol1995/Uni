from typing import Dict, List, Tuple

import numpy as np
from matplotlib import pyplot as plt


def proces_ryzyka(
    r0: float, c: float, k: int, T: float = 100, n: int = 10000
) -> np.ndarray:
    """
    Symulacja procesu ryzyka z uwzględnieniem paryskiego zegara i zmiennego lambda.

    Parametry:
        r0 (float): Kapitał początkowy
        c (float): Stała wartość zysku na jednostkę czasu
        T (float): Czas trwania symulacji
        n (int): Liczba symulacji

    Zwraca:
        np.ndarray: Macierz czasów ruiny.
    """
    times_of_ruin = np.zeros(n)

    for i in range(n):
        time = 0
        parisian_timer = 0
        ruin_time = -1
        event_times = []
        # liniowość czasu c*p(t)
        while time < T:
            lambda_ = 1 + np.sin(time)
            dt = np.random.exponential(1 / lambda_)
            time += dt
            if time >= T:
                break
            event_times.append(time)

        event_times = np.array(event_times)
        claims = np.cumsum(np.random.exponential(k, len(event_times)))
        capital_over_time = r0 + c * event_times - claims

        for j in range(len(event_times)):
            if capital_over_time[j] < -10:
                ruin_time = event_times[j]
                break

            if capital_over_time[j] < 0:
                parisian_timer += event_times[j] - (event_times[j - 1] if j > 0 else 0)
            else:
                parisian_timer = 0

            if parisian_timer > 4:
                ruin_time = event_times[j]
                break

        times_of_ruin[i] = ruin_time

    return times_of_ruin


def calculate_ruin_probability(data: np.ndarray, threshold_time: float) -> float:
    """
    Oblicza prawdopodobieństwo ruiny przed określonym czasem.

    Parametry:
        data (np.ndarray): Tablica czasów ruiny.
        threshold_time (float): Czas, przed którym liczymy prawdopodobieństwo ruiny.

    Zwraca:
        float: Prawdopodobieństwo ruiny przed threshold_time.
    """
    ruin_count = np.sum((data != -1) & (data <= threshold_time))
    probability_of_ruin = ruin_count / len(data)
    return probability_of_ruin


# Parameters numer indexu: A=6
A = 6
r0, c, k = 2 * A, A/3, A
T = 365
n = 10000
years = 5

# Symulacja procesu ryzyka
data = proces_ryzyka(r0, c, k, T, n)
prawdop = calculate_ruin_probability(data, years * T)


# Tworzenie wykresu
plt.figure(figsize=(9, 6))
plt.hist(data[data != -1], bins=80, edgecolor="k", alpha=0.8, color="coral")
plt.title("Rozkłąd ruiny")
plt.xlabel("Czas ruiny")
plt.ylabel("Częstość")
plt.grid(linestyle="--")

print(f"Prawdopodobieństwo ruiny w ciągu {years} lat wnosi: {prawdop:.2f}")


plt.tight_layout()
plt.show()
