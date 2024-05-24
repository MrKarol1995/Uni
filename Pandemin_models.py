import argparse
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def seir_model(y, t, N, beta, sigma, gamma):
    """Analogiczny program, z tą różnicą, że można podać parametry w innej kolejności"""
    S, E, I, R, _ = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    dNdt = 0  # Pochodna sumy populacji N jest zerowa
    return dSdt, dEdt, dIdt, dRdt, dNdt

def parse_arguments():
    """możliwość zmiany kolejności parametrów"""
    parser = argparse.ArgumentParser(description='SEIR Model')
    parser.add_argument('--N', type=float, default=1000, help='Wielkość populacji')
    parser.add_argument('--S0', type=float, default=999, help='Liczba podatnych osób na początku')
    parser.add_argument('--E0', type=float, default=1, help='Liczba osób w stanie inkubacji na początku')
    parser.add_argument('--I0', type=float, default=0, help='Liczba zainfekowanych osób na początku')
    parser.add_argument('--R0', type=float, default=0, help='Liczba wyzdrowiałych osób na początku')
    parser.add_argument('--beta', type=float, default=1.34, help='Wskaźnik infekcji')
    parser.add_argument('--sigma', type=float, default=0.19, help='Wskaźnik inkubacji')
    parser.add_argument('--gamma', type=float, default=0.34, help='Wskaźnik wyzdrowień')
    return parser.parse_args()


args = parse_arguments()

N = args.N
S0 = args.S0
E0 = args.E0
I0 = args.I0
R0 = args.R0
beta = args.beta
sigma = args.sigma
gamma = args.gamma

    # Warunki początkowe
y0 = S0, E0, I0, R0, N - (S0 + E0 + I0 + R0)

    # Czas
t = np.linspace(0, 100, 100)  # zakres czasu (od 0 do 100, z 100 równo odstępującymi punktami)

    # Rozwiązanie równań różniczkowych
solution = odeint(seir_model, y0, t, args=(N, beta, sigma, gamma))
S = solution[:, 0]
E = solution[:, 1]
I = solution[:, 2]
R = solution[:, 3]
N = solution[:, 4]

    # Wykres
plt.plot(t, S, label='Podatni')
plt.plot(t, E, label='W inkubacji')
plt.plot(t, I, label='Zainfekowani')
plt.plot(t, R, label='Wyzdrowiali')
plt.plot(t, N, label='Suma populacji')
plt.xlabel('Czas')
plt.ylabel('Liczba osób')
plt.legend()
plt.show()
