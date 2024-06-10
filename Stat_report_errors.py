import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

print("nowy")
#Zad 1
# Wczytanie danych z pliku
dane = np.loadtxt('dane1.txt')

# Parametry
mu_0 = 1.5  # Hipotetyczna średnia
sigma = 0.2  # Odchylenie standardowe populacji
alpha = 0.05  # Poziom istotności

# Statystyki próby
n = len(dane)
mean_sample = np.mean(dane)
std_sample = np.std(dane, ddof=1)
se = sigma / np.sqrt(n)  # Błąd standardowy

# Obliczanie statystyki t
t_stat = (mean_sample - mu_0) / se

# Testy hipotez
# H0: μ = 1.5 vs H1: μ ≠ 1.5 (dwustronny)
p_value_two_sided = 2 * (1 - stats.norm.cdf(abs(t_stat)))

# H0: μ = 1.5 vs H1: μ > 1.5 (jednostronny prawostronny)
p_value_one_sided_right = 1 - stats.norm.cdf(t_stat)

# H0: μ = 1.5 vs H1: μ < 1.5 (jednostronny lewostronny)
p_value_one_sided_left = stats.norm.cdf(t_stat)

# Wyznaczanie obszarów krytycznych
z_critical_two_sided = stats.norm.ppf(1 - alpha/2)
z_critical_one_sided = stats.norm.ppf(1 - alpha)

# Wyniki
print(f"Średnia z próby: {mean_sample}")
print(f"Statystyka t: {t_stat}")

print("\nHipoteza dwustronna H0: μ = 1.5 vs H1: μ ≠ 1.5")
print(f"p-wartość: {p_value_two_sided}")

print("\nHipoteza jednostronna H0: μ = 1.5 vs H1: μ > 1.5")
print(f"p-wartość: {p_value_one_sided_right}")

print("\nHipoteza jednostronna H0: μ = 1.5 vs H1: μ < 1.5")
print(f"p-wartość: {p_value_one_sided_left}")

# Wykresy
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x)

plt.figure(figsize=(12, 6))

# Hipoteza dwustronna
plt.subplot(1, 3, 1)
plt.plot(x, y, label='Rozkład normalny N(0, 1)')
plt.fill_between(x, 0, y, where=(abs(x) >= z_critical_two_sided), color='red', alpha=0.5, label='Obszar krytyczny')
plt.axvline(t_stat, color='blue', linestyle='--', label='Statystyka t')
plt.title('Hipoteza dwustronna')
plt.legend()

# Hipoteza jednostronna prawostronna
plt.subplot(1, 3, 2)
plt.plot(x, y, label='Rozkład normalny N(0, 1)')
plt.fill_between(x, 0, y, where=(x >= z_critical_one_sided), color='red', alpha=0.5, label='Obszar krytyczny')
plt.axvline(t_stat, color='blue', linestyle='--', label='Statystyka t')
plt.title('Hipoteza jednostronna prawostronna')
plt.legend()

# Hipoteza jednostronna lewostronna
plt.subplot(1, 3, 3)
plt.plot(x, y, label='Rozkład normalny N(0, 1)')
plt.fill_between(x, 0, y, where=(x <= -z_critical_one_sided), color='red', alpha=0.5, label='Obszar krytyczny')
plt.axvline(t_stat, color='blue', linestyle='--', label='Statystyka t')
plt.title('Hipoteza jednostronna lewostronna')
plt.legend()

plt.tight_layout()
plt.show()

#wykaz danch

# Wczytanie danych z pliku
dane = np.loadtxt('dane1.txt')

# Statystyki próby
mean_sample = np.mean(dane)
std_sample = np.std(dane, ddof=1)

# Parametry teoretycznego rozkładu normalnego
mu = mean_sample  # Średnia z próby jako estymator średniej populacji
sigma = std_sample  # Odchylenie standardowe z próby jako estymator odchylenia standardowego populacji

# Histogram danych z próby
plt.hist(dane, bins=30, density=True, alpha=0.6, color='g', label='Dane z próby')

# Zakres wartości dla rozkładu normalnego
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Gęstość teoretycznego rozkładu normalnego
p = stats.norm.pdf(x, mu, sigma)

# Wykres teoretycznego rozkładu normalnego
plt.plot(x, p, 'k', linewidth=2, label='Teoretyczny rozkład normalny')

# Dodanie etykiet i tytułu
plt.xlabel('Wartości')
plt.ylabel('Gęstość')
plt.title('Histogram danych z próby i teoretyczny rozkład normalny')
plt.legend()

# Wyświetlenie wykresu
plt.show()

#Zad 2

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Wczytanie danych z pliku
data = np.loadtxt('dane2.txt')

# Parametry problemu
alpha = 0.05
sigma2_0 = 1.5
n = len(data)
sample_variance = np.var(data, ddof=1)

# Obliczenie statystyki testowej chi-kwadrat
chi2_stat = (n - 1) * sample_variance / sigma2_0

# Weryfikacja hipotez
# Hipoteza 1: σ2 ̸= 1.5 (test dwustronny)
chi2_critical_low = stats.chi2.ppf(alpha / 2, df=n - 1)
chi2_critical_high = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
p_value_two_tailed = 2 * min(stats.chi2.cdf(chi2_stat, df=n - 1), 1 - stats.chi2.cdf(chi2_stat, df=n - 1))

# Hipoteza 2: σ2 > 1.5 (test jednostronny prawostronny)
chi2_critical_right = stats.chi2.ppf(1 - alpha, df=n - 1)
p_value_right = 1 - stats.chi2.cdf(chi2_stat, df=n - 1)

# Hipoteza 3: σ2 < 1.5 (test jednostronny lewostronny)
chi2_critical_left = stats.chi2.ppf(alpha, df=n - 1)
p_value_left = stats.chi2.cdf(chi2_stat, df=n - 1)

# Wydrukowanie wyników
print(f"Statystyka testowa chi-kwadrat: {chi2_stat:.4f}")
print(f"Hipoteza 1: σ2 ̸= 1.5")
print(f"  Obszar krytyczny: ({chi2_critical_low:.4f}, {chi2_critical_high:.4f})")
print(f"  p-wartość: {p_value_two_tailed:.4f}")
print(f"Hipoteza 2: σ2 > 1.5")
print(f"  Obszar krytyczny: ({chi2_critical_right:.4f}, ∞)")
print(f"  p-wartość: {p_value_right:.4f}")
print(f"Hipoteza 3: σ2 < 1.5")
print(f"  Obszar krytyczny: (0, {chi2_critical_left:.4f})")
print(f"  p-wartość: {p_value_left:.4f}")

# Rysowanie obszarów krytycznych
x = np.linspace(0, max(chi2_critical_high, chi2_stat) + 10, 1000)
y = stats.chi2.pdf(x, df=n - 1)

# Wykres dla hipotezy dwustronnej
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Rozkład chi-kwadrat')
plt.fill_between(x, 0, y, where=(x <= chi2_critical_low) | (x >= chi2_critical_high), color='red', alpha=0.3, label='Obszar krytyczny (dwustronny)')
plt.axvline(chi2_stat, color='black', linestyle='--', label=f'Statystyka testowa (χ² = {chi2_stat:.4f})')
plt.xlabel('Wartość χ²')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.title('Rozkład chi-kwadrat i obszar krytyczny dla hipotezy dwustronnej')
plt.legend()
plt.grid(True)
plt.show()

# Wykres dla hipotezy prawostronnej
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Rozkład chi-kwadrat')
plt.fill_between(x, 0, y, where=(x >= chi2_critical_right), color='blue', alpha=0.3, label='Obszar krytyczny (prawostronny)')
plt.axvline(chi2_stat, color='black', linestyle='--', label=f'Statystyka testowa (χ² = {chi2_stat:.4f})')
plt.xlabel('Wartość χ²')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.title('Rozkład chi-kwadrat i obszar krytyczny dla hipotezy prawostronnej')
plt.legend()
plt.grid(True)
plt.show()

# Wykres dla hipotezy lewostronnej
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Rozkład chi-kwadrat')
plt.fill_between(x, 0, y, where=(x <= chi2_critical_left), color='green', alpha=0.3, label='Obszar krytyczny (lewostronny)')
plt.axvline(chi2_stat, color='black', linestyle='--', label=f'Statystyka testowa (χ² = {chi2_stat:.4f})')
plt.xlabel('Wartość χ²')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.title('Rozkład chi-kwadrat i obszar krytyczny dla hipotezy lewostronnej')
plt.legend()
plt.grid(True)
plt.show()

# Wpływ zmiany poziomu istotności na wyniki
print("\nWpływ zmiany poziomu istotności:")
for new_alpha in [0.01, 0.1]:
    chi2_critical_low_new = stats.chi2.ppf(new_alpha / 2, df=n - 1)
    chi2_critical_high_new = stats.chi2.ppf(1 - new_alpha / 2, df=n - 1)
    p_value_two_tailed_new = 2 * min(stats.chi2.cdf(chi2_stat, df=n - 1), 1 - stats.chi2.cdf(chi2_stat, df=n - 1))

    chi2_critical_right_new = stats.chi2.ppf(1 - new_alpha, df=n - 1)
    p_value_right_new = 1 - stats.chi2.cdf(chi2_stat, df=n - 1)

    chi2_critical_left_new = stats.chi2.ppf(new_alpha, df=n - 1)
    p_value_left_new = stats.chi2.cdf(chi2_stat, df=n - 1)

    print(f"Poziom istotności α = {new_alpha}")
    print(f"  Hipoteza 1: Obszar krytyczny: ({chi2_critical_low_new:.4f}, {chi2_critical_high_new:.4f})")
    print(f"    p-wartość: {p_value_two_tailed_new:.4f}")
    print(f"  Hipoteza 2: Obszar krytyczny: ({chi2_critical_right_new:.4f}, ∞)")
    print(f"    p-wartość: {p_value_right_new:.4f}")
    print(f"  Hipoteza 3: Obszar krytyczny: (0, {chi2_critical_left_new:.4f})")
    print(f"    p-wartość: {p_value_left_new:.4f}")
    
#Zad 3
import numpy as np
import scipy.stats as stats

# Parametry symulacji
sigma2_0 = 1.5
n = 30  # Rozmiar próbki
alpha = 0.05
num_simulations = 10000

# Funkcja do generowania próbek i przeprowadzania testów
def simulate_test(true_variance, n, alpha, sigma2_0, alternative='two-sided'):
    rejections = 0
    for _ in range(num_simulations):
        sample = np.random.normal(loc=0.2, scale=np.sqrt(true_variance), size=n)
        sample_variance = np.var(sample, ddof=1)
        chi2_stat = (n - 1) * sample_variance / sigma2_0
        
        if alternative == 'two-sided':
            chi2_critical_low = stats.chi2.ppf(alpha / 2, df=n - 1)
            chi2_critical_high = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
            if chi2_stat <= chi2_critical_low or chi2_stat >= chi2_critical_high:
                rejections += 1
        elif alternative == 'greater':
            chi2_critical_right = stats.chi2.ppf(1 - alpha, df=n - 1)
            if chi2_stat >= chi2_critical_right:
                rejections += 1
        elif alternative == 'less':
            chi2_critical_left = stats.chi2.ppf(alpha, df=n - 1)
            if chi2_stat <= chi2_critical_left:
                rejections += 1
                
    return rejections / num_simulations

# Symulacja błędów I i II rodzaju oraz mocy testu dla danych z dane1.txt
print("Dane z dane1.txt:")
error_type_I_two_sided_1 = simulate_test(sigma2_0, n, alpha, sigma2_0, alternative='two-sided')
error_type_I_greater_1 = simulate_test(sigma2_0, n, alpha, sigma2_0, alternative='greater')
error_type_I_less_1 = simulate_test(sigma2_0, n, alpha, sigma2_0, alternative='less')

true_variance_greater_1 = 2.0  # Przykładowa wariancja > sigma2_0
true_variance_less_1 = 1.0      # Przykładowa wariancja < sigma2_0

error_type_II_two_sided_greater_1 = 1 - simulate_test(true_variance_greater_1, n, alpha, sigma2_0, alternative='two-sided')
error_type_II_two_sided_less_1 = 1 - simulate_test(true_variance_less_1, n, alpha, sigma2_0, alternative='two-sided')
error_type_II_greater_1 = 1 - simulate_test(true_variance_greater_1, n, alpha, sigma2_0, alternative='greater')
error_type_II_less_1 = 1 - simulate_test(true_variance_less_1, n, alpha, sigma2_0, alternative='less')

# Wydrukowanie wyników dla danych z dane1.txt
print("Błąd I rodzaju (alpha):")
print(f"Hipoteza dwustronna: {error_type_I_two_sided_1:.4f}")
print(f"Hipoteza prawostronna: {error_type_I_greater_1:.4f}")
print(f"Hipoteza lewostronna: {error_type_I_less_1:.4f}")

print("\nBłąd II rodzaju (beta) i Moc testów:")
print(f"Hipoteza dwustronna, σ2 > 1.5: Błąd II rodzaju: {error_type_II_two_sided_greater_1:.4f}, Moc: {1 - error_type_II_two_sided_greater_1:.4f}")
print(f"Hipoteza dwustronna, σ2 < 1.5: Błąd II rodzaju: {error_type_II_two_sided_less_1:.4f}, Moc: {1 - error_type_II_two_sided_less_1:.4f}")
print(f"Hipoteza prawostronna: Błąd II rodzaju: {error_type_II_greater_1:.4f}, Moc: {1 - error_type_II_greater_1:.4f}")
print(f"Hipoteza lewostronna: Błąd II rodzaju: {error_type_II_less_1:.4f}, Moc: {1 - error_type_II_less_1:.4f}")

# Symulacja błędów I i II rodzaju oraz mocy testu dla danych z dane2.txt
print("\nDane z dane2.txt:")
error_type_I_two_sided_2 = simulate_test(sigma2_0, n, alpha, sigma2_0, alternative='two-sided')
error_type_I_greater_2 = simulate_test(sigma2_0, n, alpha, sigma2_0, alternative='greater')
error_type_I_less_2 = simulate_test(sigma2_0, n, alpha, sigma2_0, alternative='less')

true_variance_greater_2 = 2.0  # Przykładowa wariancja > sigma2_0
true_variance_less_2 = 1.0      # Przykładowa wariancja < sigma2_0

error_type_II_two_sided_greater_2 = 1 - simulate_test(true_variance_greater_2, n, alpha, sigma2_0, alternative='two-sided')
error_type_II_two_sided_less_2 = 1 - simulate_test(true_variance_less_2, n, alpha, sigma2_0, alternative='two-sided')
error_type_II_greater_2 = 1 - simulate_test(true_variance_greater_2, n, alpha, sigma2_0, alternative='greater')
error_type_II_less_2 = 1 - simulate_test(true_variance_less_2, n, alpha, sigma2_0, alternative='less')

# Wydrukowanie wyników dla danych z dane2.txt
print("Błąd I rodzaju (alpha):")
print(f"Hipoteza dwustronna: {error_type_I_two_sided_2:.4f}")
print(f"Hipoteza prawostronna: {error_type_I_greater_2:.4f}")
print(f"Hipoteza lewostronna: {error_type_I_less_2:.4f}")

print("\nBłąd II rodzaju (beta) i Moc testów:")
print(f"Hipoteza dwustronna, σ2 > 1.5: Błąd II rodzaju: {error_type_II_two_sided_greater_2:.4f}, Moc: {1 - error_type_II_two_sided_greater_2:.4f}")
print(f"Hipoteza dwustronna, σ2 < 1.5: Błąd II rodzaju: {error_type_II_two_sided_less_2:.4f}, Moc: {1 - error_type_II_two_sided_less_2:.4f}")
print(f"Hipoteza prawostronna: Błąd II rodzaju: {error_type_II_greater_2:.4f}, Moc: {1 - error_type_II_greater_2:.4f}")
print(f"Hipoteza lewostronna: Błąd II rodzaju: {error_type_II_less_2:.4f}, Moc: {1 - error_type_II_less_2:.4f}")
