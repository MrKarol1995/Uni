import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable

def mieszany_proces_poissona(L_dist: Callable[[], float], T: float, liczba_traektorii: int = 10) -> List[np.ndarray]:
    """
    Generuje trajektorie mieszanego procesu Poissona.

    Args:
        L_dist (Callable[[], float]): Rozkład losowy dla lambda.
        T (float): Czas końcowy symulacji.
        liczba_traektorii (int): Liczba trajektorii do wygenerowania. 10.

    Returns:
        List[np.ndarray]: Lista trajektorii.
    """
    trajektorie = []

    for _ in range(liczba_traektorii):
        lam = L_dist()  # Generowanie lambda
        n = np.random.poisson(lam * T)  # Generowanie liczby skoków

        if n == 0:
            trajektorie.append(np.array([0]))
        else:
            U = np.sort(np.random.uniform(0, T, n))  # Generowanie i sortowanie U
            trajektorie.append(U)

    return trajektorie

# Parametry symulacji
T = 10  # Czas końcowy symulacji
liczba_traektorii = 15  # Liczba trajektorii do wygenerowania

# Rozkład lambda: L ~ U(0, 10)
trajektorie_uniform = mieszany_proces_poissona(lambda: np.random.uniform(0, 10), T, liczba_traektorii)

# Rozkład lambda: L ~ Exp(1)
trajektorie_exp = mieszany_proces_poissona(lambda: np.random.exponential(1), T, liczba_traektorii)

# Rysowanie trajektorii
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
for trajektoria in trajektorie_uniform:
    plt.step(trajektoria, np.arange(1, len(trajektoria) + 1), where="post")
plt.title("Mieszany proces Poissona z L ~ U(0, 10)")
plt.xlabel("Czas")
plt.ylabel("Liczba skoków")
plt.grid(linestyle="--")

plt.subplot(1, 2, 2)
for trajektoria in trajektorie_exp:
    plt.step(trajektoria, np.arange(1, len(trajektoria) + 1), where="post")
plt.title("Mieszany proces Poissona z L ~ Exp(1)")
plt.xlabel("Czas")
plt.ylabel("Liczba skoków")
plt.grid(linestyle="--")

plt.tight_layout()
plt.show()
