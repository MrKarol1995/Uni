import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji g(t)
def g(t, alpha):
    return np.exp(-alpha * t) * (t >= 0)

# Parametr alpha
alpha = 1.0

# Zakres czasu
t = np.linspace(-2, 5, 500)

# Obliczenie wartości funkcji g(t)
g_t = g(t, alpha)

# Wykres funkcji g(t)
plt.plot(t, g_t, label=r'$g(t) = \frac{1}{2} e^{-\alpha t} (1 + \text{sign}(t))$')
plt.xlabel('t')
plt.ylabel('g(t)')
plt.title('Wykres funkcji $g(t)$')
plt.legend()
plt.grid(True)
plt.show()


import scipy.stats as stats

# Parametry
n = 200
p = 0.04

# Obliczenie prawdopodobieństwa
P_X_leq_2 = sum([stats.binom.pmf(k, n, p) for k in range(3)])
print(P_X_leq_2)

import sympy as sp

# Define the variable and the transfer function H(s)
s = sp.symbols('s')
H_s = (12*s**2+s+1) / (s**2 + 2*s +19)

# Find zeros of H(s)
zeros = sp.solve(sp.numer(H_s), s)

# Find poles of H(s)
poles = sp.solve(sp.denom(H_s), s)

# Convert results to numerical values
zeros_num = [z.evalf() for z in zeros]
poles_num = [p.evalf() for p in poles]

print("Zeros:", zeros_num)
print("Poles:", poles_num)


import numpy as np

# Parametry sygnału i filtra
A = 16  # amplituda sygnału x(t)
omega = 13  # częstotliwość sygnału x(t)
alpha = 11  # współczynnik tłumienia filtra h(t)

# Obliczenia amplitudy sygnału po filtracji
denominator = np.sqrt(alpha**2 + omega**2)
A_new = A / denominator

# Obliczenia przesunięcia fazowego
phi = np.arctan(omega / alpha)

# Wyniki
print("Amplituda nowego sygnału:", A_new)
print("Przesunięcie fazowe (w radianach):", phi)
print("Przesunięcie fazowe (w stopniach):", np.degrees(phi))
