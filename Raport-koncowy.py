"""
Skrypt analizujący różne metody całkowania Monte Carlo oraz symulujący proces Wienera
i porównujący go z teoretycznym rozkładem arcsine.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import arcsine


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
def monte_carlo_basic(n: int) -> np.ndarray:
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
def monte_carlo_antithetic(n: int) -> np.ndarray:
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
def monte_carlo_control_variate(n: int) -> np.ndarray:
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

# Wyniki i błędy dla każdej z metod
basic_results = []
antithetic_results = []
control_variate_results = []

basic_errors = []
antithetic_errors = []
control_variate_errors = []

for n in n_values:
    basic_result = monte_carlo_basic(n)
    antithetic_result = monte_carlo_antithetic(n)
    control_variate_result = monte_carlo_control_variate(n)

    basic_error = np.abs(basic_result - exact_value)
    antithetic_error = np.abs(antithetic_result - exact_value)
    control_variate_error = np.abs(control_variate_result - exact_value)

    basic_results.append(basic_result)
    antithetic_results.append(antithetic_result)
    control_variate_results.append(control_variate_result)

    basic_errors.append(basic_error)
    antithetic_errors.append(antithetic_error)
    control_variate_errors.append(control_variate_error)

# Wykresy błędów
plt.figure(figsize=(12, 8))

plt.plot(n_values, basic_errors, marker="o", label="Monte Carlo Basic")
plt.plot(n_values, antithetic_errors, marker="s", label="Antithetic Variates")
plt.plot(n_values, control_variate_errors, marker="^", label="Control Variates")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Liczba prób")
plt.ylabel("Błąd")
plt.title("Analiza błędu względem ilości symulacji")
plt.legend()
plt.grid(linestyle="--")
plt.show()

# Wariancje dla każdej z metod
basic_variance = [np.var([monte_carlo_basic(n) for _ in range(100)]) for n in n_values]
antithetic_variance = [
    np.var([monte_carlo_antithetic(n) for _ in range(100)]) for n in n_values
]
control_variate_variance = [
    np.var([monte_carlo_control_variate(n) for _ in range(100)]) for n in n_values
]

# Wykresy wariancji
plt.figure(figsize=(12, 8))

plt.plot(n_values, basic_variance, marker="o", label="Monte Carlo Basic")
plt.plot(n_values, antithetic_variance, marker="s", label="Antithetic Variates")
plt.plot(n_values, control_variate_variance, marker="^", label="Control Variates")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Liczba prób")
plt.ylabel("Wariancja")
plt.title("Analiza wariancji względem ilości symulacji")
plt.legend()
plt.grid(linestyle="--")
plt.show()

# Generowanie wyników dla histogramów
sample_size = 1000
basic_samples = [monte_carlo_basic(n) for _ in range(sample_size)]
antithetic_samples = [monte_carlo_antithetic(n) for _ in range(sample_size)]
control_variate_samples = [monte_carlo_control_variate(n) for _ in range(sample_size)]

plt.hist(basic_samples, label="Monte Carlo", bins=50, alpha=0.3, density=True)
plt.hist(
    antithetic_samples, label="Antithetic Variance", bins=50, alpha=0.3, density=True
)
plt.hist(
    control_variate_samples, label="Control Variance", bins=50, alpha=0.3, density=True
)
plt.legend(loc="best")
plt.title("Histogram wyników symulacji każdej z metod")
plt.axvline(
    x=np.pi,
    color="r",
    linestyle="--",
    linewidth=2,
    label="Wartość teoretyczna liczby pi",
)
plt.grid(linestyle="--")
plt.show()

# Rysowanie boxplotów

plt.boxplot(
    [basic_samples, antithetic_samples, control_variate_samples],
    labels=["Monte Carlo", "Antithetic", "Control Variate"],
)
plt.axhline(exact_value, color="r", linestyle="dashed", linewidth=1)
plt.title("Boxploty dla różnych metod Monte Carlo")
plt.xlabel("Metoda")
plt.ylabel("Wynik")
plt.grid(linestyle="--")
plt.show()

# Tabela wyników i błędów
print(" ")
print(
    f"{'Liczba prób':<15} {'Wynik (Basic)':<15} {'Błąd (Basic)':<15} {'Wynik (Antithetic)':<20} "
    f"{'Błąd (Antithetic)':<20} {'Wynik (Control Variate)':<25} {'Błąd (Control Variate)':<25}"
)
for (
    n,
    basic_result,
    basic_error,
    antithetic_result,
    antithetic_error,
    control_variate_result,
    control_variate_error,
) in zip(
    n_values,
    basic_results,
    basic_errors,
    antithetic_results,
    antithetic_errors,
    control_variate_results,
    control_variate_errors,
):
    print(
        f"{n:<15} {basic_result:<15.10f} {basic_error:<15.10f} {antithetic_result:<20.10f}"
        f" {antithetic_error:<20.10f} {control_variate_result:<25.10f} {control_variate_error:<25.10f}"
    )


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
axs[0, 0].grid(linestyle="--")

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
axs[0, 1].grid(linestyle="--")

# Histogram dla L
axs[1, 0].hist(L, bins=50, density=True, alpha=0.6, color="coral", label="Empiryczny")
axs[1, 0].plot(x, arcsine.pdf(x), "r-", lw=2, label="Teoretyczny")
axs[1, 0].set_title("Histogram L")
axs[1, 0].legend()
axs[1, 0].grid(linestyle="--")

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
axs[1, 1].grid(linestyle="--")

# Histogram dla M
axs[2, 0].hist(M, bins=50, density=True, alpha=0.6, color="coral", label="Empiryczny")
axs[2, 0].plot(x, arcsine.pdf(x), "r-", lw=2, label="Teoretyczny")
axs[2, 0].set_title("Histogram M")
axs[2, 0].legend()
axs[2, 0].grid(linestyle="--")

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
axs[2, 1].grid(linestyle="--")

plt.tight_layout()
plt.show()
