import numpy as np
import matplotlib.pyplot as plt


#Kolos
#c
np.random.seed(42)

mu = 3
sigma = 2
n = 10
m = 1000

# Symulacja Monte Carlo
means = []
thetas = []

for _ in range(m):
    sample = np.random.normal(mu, sigma, n)
    mean_estimator = np.mean(sample)
    theta_estimator = (2 * sample[0] + 3 * sample[1] - 2 * sample[-1]) / 3

    means.append(mean_estimator)
    thetas.append(theta_estimator)

# Obliczanie średniej i wariancji estymatorów
mean_mean = np.mean(means)
mean_var = np.var(means)
theta_mean = np.mean(thetas)
theta_var = np.var(thetas)

print(f'Estymator średniej: Średnia = {mean_mean}, Wariancja = {mean_var}')
print(f'Estymator θ: Średnia = {theta_mean}, Wariancja = {theta_var}')

# Histogramy estymatorów
plt.figure(figsize=(12, 6))

# Ustawienia histogramu dla estymatora średniej
plt.subplot(1, 2, 1)
plt.hist(means, bins=30, density=True, alpha=0.6, color='g')
plt.title('Estymator średniej')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')

# Ustawienia histogramu dla estymatora θ
plt.subplot(1, 2, 2)
plt.hist(thetas, bins=30, density=True, alpha=0.6, color='r')
plt.title('Estymator θ')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')

# Znalezienie wspólnych granic dla osi x i y
all_values = np.concatenate((means, thetas))
x_min, x_max = all_values.min(), all_values.max()

# Ustawienie tych samych granic osi x i y dla obu wykresów
plt.subplot(1, 2, 1)
plt.xlim(x_min, x_max)
plt.ylim(0, plt.subplot(1, 2, 1).get_ylim()[1])

plt.subplot(1, 2, 2)
plt.xlim(x_min, x_max)
plt.ylim(0, plt.subplot(1, 2, 2).get_ylim()[1])

plt.tight_layout()
plt.show()

#e
import scipy.stats as stats

# Parametry rozkładów teoretycznych
theoretical_mean_dist = stats.norm(mu, sigma/np.sqrt(n))
theoretical_theta_dist = stats.norm(mu, np.sqrt(17/9)*sigma)

# Symulacja wartości estymatorów
means = np.random.normal(mu, sigma/np.sqrt(n), m)
thetas = np.random.normal(mu, np.sqrt(17/9)*sigma, m)

# Porównanie dystrybuant
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sorted_means = np.sort(means)
plt.plot(sorted_means, np.linspace(0, 1, m, endpoint=False), label='Empiryczna dystrybuanta')
plt.plot(sorted_means, theoretical_mean_dist.cdf(sorted_means), label='Teoretyczna dystrybuanta', linestyle='dashed')
plt.title('Dystrybuanta estymatora średniej')
plt.xlabel('Wartość')
plt.ylabel('Dystrybuanta')
plt.legend()

plt.subplot(1, 2, 2)
sorted_thetas = np.sort(thetas)
plt.plot(sorted_thetas, np.linspace(0, 1, m, endpoint=False), label='Empiryczna dystrybuanta')
plt.plot(sorted_thetas, theoretical_theta_dist.cdf(sorted_thetas), label='Teoretyczna dystrybuanta', linestyle='dashed')
plt.title('Dystrybuanta estymatora θ')
plt.xlabel('Wartość')
plt.ylabel('Dystrybuanta')
plt.legend()

plt.tight_layout()
plt.show()

# Porównanie gęstości
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(means, bins=30, density=True, alpha=0.6, color='g', label='Empiryczna gęstość')
x = np.linspace(min(means), max(means), 100)
plt.plot(x, theoretical_mean_dist.pdf(x), 'k', linewidth=2, label='Teoretyczna gęstość')
plt.title('Gęstość estymatora średniej')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(thetas, bins=30, density=True, alpha=0.6, color='r', label='Empiryczna gęstość')
x = np.linspace(min(thetas), max(thetas), 100)
plt.plot(x, theoretical_theta_dist.pdf(x), 'k', linewidth=2, label='Teoretyczna gęstość')
plt.title('Gęstość estymatora θ')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')
plt.legend()

plt.tight_layout()
plt.show()

