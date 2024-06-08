import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto, lognorm

# Parametry rozkładów
b = 2.62  # parametr kształtu rozkładu Pareto
s = 0.9  # parametr skali (sigma) rozkładu log-normalnego
scale_lognorm = np.exp(0)  # parametr skali (mu) rozkładu log-normalnego

# Liczba próbek
n_samples = 1000

# Generowanie próbek
samples_pareto = pareto.rvs(b, size=n_samples)
samples_lognorm = lognorm.rvs(s, scale=scale_lognorm, size=n_samples)

# Zakres wartości dla porównania
x = np.linspace(1, 10, 1000)

# Gęstość rozkładu Pareto
pdf_pareto = pareto.pdf(x, b)

# Gęstość rozkładu log-normalnego
pdf_lognorm = lognorm.pdf(x, s, scale=scale_lognorm)

# Dystrybuanta rozkładu Pareto
cdf_pareto = pareto.cdf(x, b)

# Dystrybuanta rozkładu log-normalnego
cdf_lognorm = lognorm.cdf(x, s, scale=scale_lognorm)

# Wykres gęstości
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.hist(samples_pareto, bins=60, density=True, alpha=0.6, color='blue', label='Empiryczna Pareto')
plt.plot(x, pdf_pareto, 'r-', lw=2, label='Teoretyczna Pareto')
plt.title('Gęstość rozkładu Pareto')
plt.xlabel('x')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend()

plt.subplot(2, 2, 2)
plt.hist(samples_lognorm, bins=60, density=True, alpha=0.6, color='green', label='Empiryczna Log-normal')
plt.plot(x, pdf_lognorm, 'r-', lw=2, label='Teoretyczna Log-normal')
plt.title('Gęstość rozkładu Log-normal')
plt.xlabel('x')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend()

# Wykres dystrybuanty
plt.subplot(2, 2, 3)
plt.plot(x, cdf_pareto, 'r-', lw=2, label='Teoretyczna Pareto')
plt.hist(samples_pareto, bins=60, density=True, alpha=0.6, color='blue', cumulative=True, label='Empiryczna Pareto')
plt.title('Dystrybuanta rozkładu Pareto')
plt.xlabel('x')
plt.ylabel('Dystrybuanta')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, cdf_lognorm, 'r-', lw=2, label='Teoretyczna Log-normal')
plt.hist(samples_lognorm, bins=60, density=True, alpha=0.6, color='green', cumulative=True, label='Empiryczna Log-normal')
plt.title('Dystrybuanta rozkładu Log-normal')
plt.xlabel('x')
plt.ylabel('Dystrybuanta')
plt.legend()

plt.tight_layout()
plt.show()
