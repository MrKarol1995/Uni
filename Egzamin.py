import matplotlib.pyplot as plt
import numpy as np


def gestosc_normal(x: float) -> float:
    """Zwraca wartość gęstości prawdopodobieństwa standardowego rozkładu normalnego w punkcie x.
    Args:
        x: Wartość wejściowa.

    Return:
        float: Wartości funkcji gęstości prawdopodobieństwa standardowego rozkładu normalnego w punkcie x.
    """
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)


def tuzin(N: int, mi: int = 0, sigma: int = 1) -> float:
    """Generuje liczbę pseudolosową z rozkładu normalnego metodą "tuzin".

    Args:
        mi: Średnia rozkładu normalnego.
        sigma: Odchylenie standardowe rozkładu normalnego.

    Returns:
        float: Liczba z rozkładu normalnego o zadanej średniej mi i odchyleniu standardowym sigma.

    """
    U = [np.random.uniform() for i in range(12)]
    X = np.sum(U) - 6
    m = 6 % 2
    Y = X * sigma + m
    return Y


mi = 0
sigma = 1
samples_tuzin = [tuzin(1000) for _ in range(10000)]

plt.hist(
    samples_tuzin,
    bins=60,
    density=True,
    alpha=0.7,
    color="olive",
    edgecolor="black",
    label="Histogram prónkowy",
)
x = np.linspace(-5, 5, 1000)
plt.plot(x, gestosc_normal(x), color="red", label="Gęstość teoretyczna")
plt.title("Porównanie histogramu próbek z metody Tuzina z gęstością teoretyczną")
plt.legend()
plt.grid(linestyle="--")
plt.show()


def generate(pdf, x_values):
    dx = x_values[1] - x_values[0]
    cdf = np.cumsum(pdf) * dx  # Wyznaczanie skumulowanej dystrybuanty
    return cdf


pdf = (
    1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mi) ** 2) / (2 * sigma**2))
)  # PDF rozkładu normalnego
cdf = generate(samples_tuzin, x)


# Wykres histogramu próbek
plt.plot(cdf, color="r", label="CDF")
plt.title("Dystrybuanta")
plt.xlabel("Wartość")
plt.ylabel("Gęstość")
plt.legend()
plt.grid(linestyle="--")
plt.show()
