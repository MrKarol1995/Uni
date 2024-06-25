import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


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
    U = [np.random.uniform() for _ in range(12)]
    X = np.sum(U) - 6
    Y = X * sigma + mi
    return Y


# Parametry rozkładu
mi = 0
sigma = 1

# Generowanie próbek
samples_tuzin = [tuzin(1000) for _ in range(10000)]

# Histogram próbek
plt.hist(
    samples_tuzin,
    bins=60,
    density=True,
    alpha=0.7,
    color="olive",
    edgecolor="black",
    label="Histogram próbek",
)
x = np.linspace(-5, 5, 1000)
plt.plot(x, gestosc_normal(x), color="red", label="Gęstość teoretyczna")
plt.title("Porównanie histogramu próbek z metody Tuzina z gęstością teoretyczną")
plt.legend()
plt.grid(linestyle="--")
plt.show()

# Dystrybuanta empiryczna vs teoretyczna
samples_sorted = np.sort(samples_tuzin)
ecdf = np.arange(1, len(samples_sorted) + 1) / len(samples_sorted)
plt.step(samples_sorted, ecdf, label="Dystrybuanta empiryczna")
plt.plot(x, stats.norm.cdf(x), color="red", label="Dystrybuanta teoretyczna")
plt.title("Porównanie dystrybuant")
plt.xlabel("Wartość")
plt.ylabel("Dystrybuanta")
plt.legend()
plt.grid(linestyle="--")
plt.show()

# QQ-plot
stats.probplot(samples_tuzin, dist="norm", plot=plt)
plt.title("Wykres kwantylowy (QQ-plot)")
plt.grid(linestyle="--")
plt.show()
