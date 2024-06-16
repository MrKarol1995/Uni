import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, List, Tuple


# Funkcja, która zwraca wartość funkcji zysków p(t)
def profit_function(t: float) -> float:
    """
    Funkcja zysków w zależności od czasu t.

    Args:
        t (float): Czas.

    Returns:
        float: Zysk w czasie t.
    """
    return 10 + np.sin(t * np.pi / 4) / 2


def simulate_risk_process(
    r0: float,
    lambda_: float,
    T: float,
    damage_distribution: Callable[[], float],
    profit_function: Callable[[float], float],
) -> Tuple[List[float], List[float]]:
    """
    Symuluje proces ryzyka.

    Args:
        r0 (float): Początkowy kapitał.
        lambda_ (float): Intensywność procesu Poissona.
        T (float): Maksymalny czas symulacji.
        damage_distribution (Callable[[], float]): Funkcja generująca szkody według zadanego rozkładu.
        profit_function (Callable[[float], float]): Funkcja zysków w zależności od czasu t.

    Returns:
        Tuple[List[float], List[float]]: Lista czasów i odpowiadających im wartości kapitału.
    """
    t = 0  # Początkowy czas
    R = r0  # Początkowy kapitał
    times = [t]
    capitals = [R]

    while t < T and R > 0:
        # Generowanie czasu do następnego zdarzenia (proces Poissona)
        dt = np.random.exponential(1 / lambda_)
        t += dt

        if t >= T:
            break

        # Liczba szkód w okresie między zdarzeniami
        num_damages = np.random.poisson(lambda_ * dt)

        # Suma szkód według zadanego rozkładu
        total_damage = sum(damage_distribution() for _ in range(num_damages))

        # Aktualizacja kapitału
        R = R + profit_function(t) - total_damage * 2.1

        # Zapisanie czasu i kapitału
        times.append(t)
        capitals.append(R)

        if R <= 0:
            break

    return times, capitals


# Funkcja użytkownika do generowania szkód z rozkładu gamma
def gamma_damage_distribution_1(shape: float = 2, scale: float = 2) -> float:
    """
    Generuje szkody z rozkładu gamma.

    Args:
        shape (float): Kształt rozkładu gamma.
        scale (float): Skala rozkładu gamma.

    Returns:
        float: Wygenerowana szkoda.
    """
    return np.random.gamma(shape, scale)


def gamma_damage_distribution_2(shape: float = 5, scale: float = 1) -> float:
    """
    Generuje szkody z rozkładu gamma.

    Args:
        shape (float): Kształt rozkładu gamma.
        scale (float): Skala rozkładu gamma.

    Returns:
        float: Wygenerowana szkoda.
    """
    return np.random.gamma(shape, scale)


# Funkcja użytkownika do generowania szkód z rozkładu Pareto
def pareto_damage_distribution(b: float = 2, scale: float = 1) -> float:
    """
    Generuje szkody z rozkładu Pareto.

    Args:
        b (float): Parametr kształtu rozkładu Pareto.
        scale (float): Skala rozkładu Pareto.

    Returns:
        float: Wygenerowana szkoda.
    """
    return (np.random.pareto(b) + 1) * scale


# Parametry symulacji
r0 = 100  # Początkowy kapitał
lambda_ = 0.4  # Intensywność procesu Poissona
T = 100  # Maksymalny czas symulacji

# Symulacja dla pierwszego rozkładu szkód (Gamma(2, 2))
times1, capitals1 = simulate_risk_process(
    r0, lambda_, T, gamma_damage_distribution_1, profit_function
)

# Symulacja dla drugiego rozkładu szkód (Gamma(5, 1))
times2, capitals2 = simulate_risk_process(
    r0, lambda_, T, gamma_damage_distribution_2, profit_function
)

# Symulacja dla trzeciego rozkładu szkód (Pareto)
times3, capitals3 = simulate_risk_process(
    r0, lambda_, T, pareto_damage_distribution, profit_function
)

# Wykres
plt.plot(times1, capitals1, drawstyle="steps-post", label="Gamma(2, 2)")
plt.plot(times2, capitals2, drawstyle="steps-post", label="Gamma(5, 1)")
plt.plot(times3, capitals3, drawstyle="steps-post", label="Pareto(2)")
plt.xlabel("Czas")
plt.ylabel("Kapitał")
plt.title("Porównanie trajektorii procesu ryzyka")
plt.legend()
plt.grid(linestyle="--")
plt.show()
