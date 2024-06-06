import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List

def mixed_poisson_process_uniform(T: float) -> Tuple[int, np.ndarray]:
    """
    Generuje trajektorię procesu Poissona z wartością lambda z rozkładu jednostajnego.

    Parametry:
    - T (float): Czas zakończenia procesu.

    Zwraca krotkę (I, S), gdzie:
    - I (int): Liczba zdarzeń.
    - S (array): Tablica zawierająca czasy zdarzeń.
    """
    lmbda = np.random.uniform(0, 10)  # Generowanie losowej wartości lambda z rozkładu jednostajnego
    t = 0
    I = 0
    S = []
    while True:
        U = np.random.rand()
        t -= (1 / lmbda) * np.log(U)
        if t > T:
            break
        I += 1
        S.append(t)
    return I, np.array(S)

def mixed_poisson_process_exponential(T: float) -> Tuple[int, np.ndarray]:
    """
    Generuje trajektorię procesu Poissona z wartością lambda z rozkładu wykładniczego.

    Parametry:
    - T (float): Czas zakończenia procesu.

    Zwraca krotkę (I, S), gdzie:
    - I (int): Liczba zdarzeń.
    - S (array): Tablica zawierająca czasy zdarzeń.
    """
    lmbda = np.random.exponential(1)  # Generowanie losowej wartości lambda z rozkładu wykładniczego
    t = 0
    I = 0
    S = []
    while True:
        U = np.random.rand()
        t -= (1 / lmbda) * np.log(U)
        if t > T:
            break
        I += 1
        S.append(t)
    return I, np.array(S)

# Parametr czasu T
T_val = 29

# Generowanie i rysowanie trajektorii
plt.figure(figsize=(15, 6))

# Generowanie trajektorii dla rozkładu jednostajnego
plt.subplot(1, 2, 1)
plt.title('10 trajektorii dla lambda z rozkładu jednostajnego')
for _ in range(10):
    I, S = mixed_poisson_process_uniform(T_val)
    plt.step(S, np.arange(len(S)), where='post', label=f'Trajektoria')
plt.xlabel('Czas')
plt.ylabel('Liczba zdarzeń')
plt.legend()
plt.grid(linestyle='--')

# Generowanie trajektorii dla rozkładu wykładniczego
plt.subplot(1, 2, 2)
plt.title('10 trajektorii dla lambda z rozkładu wykładniczego')
for _ in range(10):
    I, S = mixed_poisson_process_exponential(T_val)
    plt.step(S, np.arange(len(S)), where='post', label=f'Trajektoria')
plt.xlabel('Czas')
plt.ylabel('Liczba zdarzeń')
plt.legend()
plt.grid(linestyle='--')

plt.tight_layout()
plt.show()
