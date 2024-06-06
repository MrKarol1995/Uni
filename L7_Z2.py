import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable


def poisson_process(
    lam: float,
    time: float,
    jump_distribution: Callable[[int], np.ndarray],
    size: int = 1000,
) -> List[Tuple[np.ndarray, np.ndarray]]:
    """
    Generates trajectories of a compound Poisson process.

    Args:
        lam (float): Intensity of the Poisson process.
        time (float): End time of the simulation.
        jump_distribution (Callable[[int], np.ndarray]): Function generating jumps.
        size (int, optional): Number of trajectories to generate. Defaults to 1000.

    Returns:
        List[Tuple[np.ndarray, np.ndarray]]: List of trajectories as tuples (jump_times, Y_t).
    """
    jump_counts = np.random.poisson(lam * time, size=size)

    trajectories = []
    for count in jump_counts:
        if count == 0:
            trajectories.append((np.array([0]), np.array([0])))
        else:
            jump_times = np.sort(np.random.uniform(0, time, count))
            jumps = jump_distribution(count)
            Y_t = np.cumsum(jumps)
            trajectories.append((jump_times, Y_t))

    return trajectories


def poisson_characteristic_function(
    t: np.ndarray, lam: float, jump_char_function: Callable[[np.ndarray], np.ndarray]
) -> np.ndarray:
    """
    Computes the characteristic function of a compound Poisson process.

    Args:
        t (np.ndarray): Values for which the function is computed.
        lam (float): Intensity of the Poisson process.
        jump_char_function (Callable[[np.ndarray], np.ndarray]): Characteristic function of jumps.

    Returns:
        np.ndarray: Values of the characteristic function for the given t values.
    """
    return np.exp(lam * (jump_char_function(t) - 1))


def normal_jump_characteristic_function(t: np.ndarray) -> np.ndarray:
    """
    Computes the characteristic function for jumps from the normal distribution N(0, 1).

    Args:
        t (np.ndarray): Values for which the function is computed.

    Returns:
        np.ndarray: Values of the characteristic function for the given t values.
    """
    return np.exp(-0.5 * t ** 2)


def cauchy_jump_characteristic_function(t: np.ndarray) -> np.ndarray:
    """
    Computes the characteristic function for jumps from the Cauchy distribution C(0, 1).

    Args:
        t (np.ndarray): Values for which the function is computed.

    Returns:
        np.ndarray: Values of the characteristic function for the given t values.
    """
    return np.exp(1j * t - np.abs(t))


# Simulation parameters
lam = 1  # Intensity of the Poisson process
time = 10  # End time of the simulation
size = 3  # Number of trajectories to generate

# Simulation for jumps from the normal distribution N(0, 1)
normal_trajectories = poisson_process(
    lam, time, lambda n: np.random.normal(0, 1, n), size
)

# Simulation for jumps from the Cauchy distribution C(0, 1)
cauchy_trajectories = poisson_process(
    lam, time, lambda n: np.random.standard_cauchy(n), size
)

# Plot trajectories
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
for t, Y_t in normal_trajectories:
    if len(t) > 1:
        plt.step(t, Y_t, where="post")
plt.title("Compound Poisson Process with N(0, 1) jumps")
plt.xlabel("Time")
plt.ylabel("Y(t)")
plt.grid(linestyle="--")

plt.subplot(1, 2, 2)
for t, Y_t in cauchy_trajectories:
    if len(t) > 1:
        plt.step(t, Y_t, where="post")
plt.title("Compound Poisson Process with C(0, 1) jumps")
plt.xlabel("Time")
plt.ylabel("Y(t)")
plt.grid(linestyle="--")

plt.tight_layout()
plt.show()

# Verification of simulation correctness - characteristic function
t_values = np.linspace(-10, 10, 400)

normal_characteristic = poisson_characteristic_function(
    t_values, lam, normal_jump_characteristic_function
)
cauchy_characteristic = poisson_characteristic_function(
    t_values, lam, cauchy_jump_characteristic_function
)

# Plot characteristic functions
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(t_values, normal_characteristic.real, label="Re(φ(t))")
plt.plot(
    t_values, normal_characteristic.imag, label="Im(φ(t))", linestyle="--"
)
plt.title("Characteristic Function - Compound Poisson Process with N(0, 1) Jumps")
plt.xlabel("t")
plt.ylabel("φ(t)")
plt.legend()
plt.grid(linestyle="--")

plt.subplot(1, 2, 2)
plt.plot(t_values, cauchy_characteristic.real, label="Re(φ(t))")
plt.plot(t_values, cauchy_characteristic.imag, label="Im(φ(t))", linestyle="--")
plt.title("Characteristic Function - Compound Poisson Process with C(0, 1) Jumps")
plt.xlabel("t")
plt.ylabel("φ(t)")
plt.legend()
plt.grid(linestyle="--")

plt.tight_layout()
plt.show()
