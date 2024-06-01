"""
Skrypt analizujący różne metody całkowania Monte Carlo oraz symulujący proces Wienera
i porównujący go z teoretycznym rozkładem arcsine.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import arcsine


# Zad1 (z listy 3)


# Funkcja podcałkowa
def f(x: np.ndarray) -> np.ndarray:
    """
    Funkcja podcałkowa.

    Args:
        x (np.ndarray): Array  wartości x.

    Returns:
        np.ndarray: Oblicza wartość funkcji: 4 / (1 + x**2).
    """
    return 4 / (1 + x**2)


# Monte Carlo klasyczna
def monte_carlo_basic(n: int) -> float:
    """
    Monte Carlo całkowanie bez "redukcji wariancji."

    Args:
        n (int): Wielkość próby.

    Returns:
        float: Szanowana wartość całki.
    """
    x = np.random.uniform(0, 1, n)
    return np.mean(f(x))


# Metoda odbić lustrzanych
def monte_carlo_antithetic(n):
    """
     Całkowanie Monte Carlo przy użyciu: antithetic variates method.

    Args:
        n (int): Wielkość próby.

    Returns:
        float: Szanowana wartość całki.
    """
    x = np.random.uniform(0, 1, n // 2)
    y = 1 - x
    return np.mean((f(x) + f(y)) / 2)


# Metoda zmiennej kontrolnej (użyjemy funkcji liniowej jako zmiennej kontrolnej)
def monte_carlo_control_variate(n: int) -> float:
    """
    Monte Carlo integration using control variates method.

    Args:
        n (int): Wielkość próby.

    Returns:
        float: Szanowana wartość całki.
    """
    x = np.random.uniform(0, 1, n)
    control_variate = x
    mean_control_variate = 0.5
    y = f(x)
    alpha = np.cov(y, control_variate)[0, 1] / np.var(control_variate)
    return np.mean(y - alpha * (control_variate - mean_control_variate))


# Wielkość próby:
n = 100000

# Zastosowanie funkcji
basic_result = monte_carlo_basic(n)
antithetic_result = monte_carlo_antithetic(n)
control_variate_result = monte_carlo_control_variate(n)

# Wyniki
print(f"Wynik Monte Carlo bez redukcji wariancji: {basic_result}")
print(f"Wynik metody odbić lustrzanych: {antithetic_result}")
print(f"Wynik metody zmiennej kontrolnej: {control_variate_result}")

# Dokładna wartość całki
exact_value = np.pi

# Liczby prób
n_values = [10, 100, 200, 1000, 5000, 10000, 100000]

# Wyniki i błędy
results = []
errors = []

for n in n_values:
    result = monte_carlo_basic(n)
    error = np.abs(result - exact_value)
    results.append(result)
    errors.append(error)


# Wykres błędu
plt.figure(figsize=(10, 6))
plt.plot(n_values, errors, marker="o")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Liczba prób")
plt.ylabel("Błąd")
plt.title("Analiza błędu względem ilości symulacji")
plt.grid(True)
plt.show()

# Tabela wyników
print(" ")
print(f"{'Liczba prób':<15} {'Wynik':<15} {'Błąd':<15}")
for n, result, error in zip(n_values, results, errors):
    print(f"{n:<15} {result:<15.10f} {error:<15.10f}")


# zad2 (z listy 6)

# Liczba symulacji
n_simulations = 10000
n_steps = 1000
t = np.linspace(0, 1, n_steps + 1)


# Funkcja generująca proces Wienera
def generate_wiener_process(n_steps: int) -> np.ndarray:
    """
    Generuje Proces Wienera.

    Args:
        n_steps (int): Liczba kroków w procesie.

    Returns:
        np.ndarray: Wysymulowany proces Wienera
    """
    dt = 1 / n_steps
    dW = np.random.normal(0, np.sqrt(dt), n_steps)
    W = np.concatenate(([0], np.cumsum(dW)))
    return W


# Listy wynikowe.
T_plus = []
L = []
M = []

# Generowanie wszystkoch jednoczeście, ale każda wersja odpowianio według swojej definiji.
# Symulacja procesu Wienera oraz zbieranie danych

for _ in range(n_simulations):
    # Generowanie procesu Wienera
    W = generate_wiener_process(n_steps)

    # Obliczanie T_+
    T_plus.append(np.sum(W > 0) / n_steps)

    # Znajdowanie punktów przecięcia z zerem
    zero_crossings = np.where(np.diff(np.sign(W)))[0]

    # Sprawdzenie czy istnieją punkty przecięcia z zerem
    if zero_crossings.size > 0:
        # Jeśli istnieją, dodaj ostatni czas przecięcia z zerem przed zakończeniem symulacji do listy L
        L.append(t[zero_crossings[-1]])
    else:
        # Jeśli nie istnieją, dodaj 0 do listy L
        L.append(0)

    # Dodawanie czasu osiągnięcia maksimum do listy M
    M.append(t[np.argmax(W)])

# Histogramy oraz dystrybuanty empiryczne i teoretyczne
fig, axs = plt.subplots(3, 2, figsize=(14, 7))

# Histogram dla T_+
axs[0, 0].hist(
    T_plus, bins=50, density=True, alpha=0.6, color="coral", label="Empiryczny"
)
x = np.linspace(0, 1, 100)
axs[0, 0].plot(x, arcsine.pdf(x), "r-", lw=2, label="Teoretyczny")
axs[0, 0].set_title("Histogram T_+")
axs[0, 0].legend()

# Dystrybuanty dla T_+
axs[0, 1].hist(
    T_plus,
    bins=50,
    density=True,
    cumulative=True,
    alpha=0.6,
    color="coral",
    label="Empiryczny",
)
axs[0, 1].plot(x, arcsine.cdf(x), "r-", lw=2, label="Teoretyczny")
axs[0, 1].set_title("Dystrybuanta empiryczna T_+")
axs[0, 1].legend()

# Histogram dla L
axs[1, 0].hist(L, bins=50, density=True, alpha=0.6, color="coral", label="Empiryczny")
axs[1, 0].plot(x, arcsine.pdf(x), "r-", lw=2, label="Teoretyczny")
axs[1, 0].set_title("Histogram L")
axs[1, 0].legend()

# Dystrybuanty dla L
axs[1, 1].hist(
    L,
    bins=50,
    density=True,
    cumulative=True,
    alpha=0.6,
    color="coral",
    label="Empiryczny",
)
axs[1, 1].plot(x, arcsine.cdf(x), "r-", lw=2, label="Teoretyczny")
axs[1, 1].set_title("Dystrybuanta empiryczna L")
axs[1, 1].legend()

# Histogram dla M
axs[2, 0].hist(M, bins=50, density=True, alpha=0.6, color="coral", label="Empiryczny")
axs[2, 0].plot(x, arcsine.pdf(x), "r-", lw=2, label="Teoretyczny")
axs[2, 0].set_title("Histogram M")
axs[2, 0].legend()

# Dystrybuanty dla M
axs[2, 1].hist(
    M,
    bins=50,
    density=True,
    cumulative=True,
    alpha=0.6,
    color="coral",
    label="Empiryczny",
)
axs[2, 1].plot(x, arcsine.cdf(x), "r-", lw=2, label="Teoretyczny")
axs[2, 1].set_title("Dystrybuanta empiryczna M")
axs[2, 1].legend()

plt.tight_layout()
plt.show()
