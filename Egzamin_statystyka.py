import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

# kod do zadań a i b
# Parametr theta
theta = 8

# Liczba próbek
n = 1000

# Generowanie próbek U z rozkładu jednostajnego na przedziale (0, 1)
U = np.random.uniform(0, 1, n)

# Transformacja próbek U do próbek X
X = U**(1/theta)

# Empiryczna dystrybuanta
ecdf = np.arange(1, n+1) / n

# Sortowanie próbek X
X_sorted = np.sort(X)

# Dystrybuanta teoretyczna
F_theoretical = X_sorted

# Wykres dystrybuanty empirycznej i teoretycznej
plt.figure(figsize=(10, 6))
plt.step(X_sorted, ecdf, label='Empiryczna dystrybuanta')
plt.plot(X_sorted, F_theoretical, label='Teoretyczna dystrybuanta', linestyle='--')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.title('Porównanie dystrybuanty empirycznej i teoretycznej')
plt.grid()
plt.show()



import numpy as np
import matplotlib.pyplot as plt


#Kod do zadań d i e)
# Parametry
theta = 8
n = 10  # liczba zmiennych losowych X_i
M = 1000  # liczba prób

# Funkcje teoretyczne
def F_U(u, theta, n):
    return (1 - np.exp(-theta * u)) ** n

def f_U(u, theta, n):
    return n * theta * np.exp(-theta * u) * (1 - np.exp(-theta * u)) ** (n - 1)

# Generowanie M wartości statystyki U
U_samples = np.max(np.random.exponential(scale=1/theta, size=(M, n)), axis=1)

# Empiryczna dystrybuanta
empirical_cdf = np.sort(U_samples)
empirical_cdf_y = np.arange(1, M+1) / M

# Wartości do wykresów teoretycznych
u_values = np.linspace(0, np.max(U_samples), 1000)
theoretical_cdf = F_U(u_values, theta, n)

# Wykres porównawczy dystrybuant
plt.figure(figsize=(10, 6))
plt.step(empirical_cdf, empirical_cdf_y, where='post', label='Empiryczna dystrybuanta')
plt.plot(u_values, theoretical_cdf, label='Teoretyczna dystrybuanta', color='red')
plt.xlabel('u')
plt.ylabel('Dystrybuanta')
plt.title('Porównanie empirycznej i teoretycznej dystrybuanty')
plt.legend()
plt.grid(True)
plt.show()

# Wykres funkcji gęstości
theoretical_pdf = f_U(u_values, theta, n)
plt.figure(figsize=(10, 6))
plt.hist(U_samples, bins=30, density=True, alpha=0.6, color='g', label='Empiryczna gęstość')
plt.plot(u_values, theoretical_pdf, label='Teoretyczna funkcja gęstości', color='red')
plt.xlabel('u')
plt.ylabel('Gęstość')
plt.title('Porównanie empirycznej i teoretycznej funkcji gęstości')
plt.legend()
plt.grid(True)
plt.show()
