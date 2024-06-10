import numpy as np
import matplotlib.pyplot as plt
#podkpunkt c

mu = 3
sigma = 2
n = 10
m = 1000

def estymator_theta(X):
    return (2*X[0] + 3*X[1] - 2*X[9]) / 3


estymatory_mu = []
estymatory_theta = []

for _ in range(m):
    X = np.random.normal(mu, sigma, n)
    est_mu = np.mean(X)
    est_theta = estymator_theta(X)
    estymatory_mu.append(est_mu)
    estymatory_theta.append(est_theta)


mean_mu = np.mean(estymatory_mu)
var_mu = np.var(estymatory_mu)
mean_theta = np.mean(estymatory_theta)
var_theta = np.var(estymatory_theta)

print(f'Estymator mu: średnia = {mean_mu}, wariancja = {var_mu}')
print(f'Estymator theta: średnia = {mean_theta}, wariancja = {var_theta}')

plt.figure(figsize=(10, 6))
plt.boxplot([estymatory_mu, estymatory_theta], labels=['Estymator mu', 'Estymator theta'])
plt.title('Box plot estymatorów mu i theta')
plt.ylabel('Wartości estymatorów')
plt.grid(linestyle='--')
plt.show()

#podpunkt e

import matplotlib.pyplot as plt
import seaborn as sns


sim_mu = []
sim_theta = []

for _ in range(1000):
    X = np.random.normal(mu, sigma, n)
    sim_mu.append(np.mean(X))
    sim_theta.append(estymator_theta(X))

sns.kdeplot(sim_mu, label='Estymator mu')
sns.kdeplot(sim_theta, label='Estymator theta')
plt.legend()
plt.grid(linestyle='--')
plt.show()