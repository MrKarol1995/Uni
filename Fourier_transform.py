import numpy as np
import matplotlib.pyplot as plt

#Karol Cieślik
#Analiza Fouriera
# Parametry sygnału
sampling_rate = 1000  # Częstotliwość próbkowania (Hz)
T = 1.0 / sampling_rate  # Okres próbkowania
t = np.arange(0, 1.0, T)  # Wezły czasowe od 0 do 1 sekundy

# Generowanie sygnału złożonego z kilku częstotliwości
f1 = 50  # Częstotliwość pierwszego sygnału (Hz)
f2 = 120  # Częstotliwość drugiego sygnału (Hz)
f3 = 180  # Częstotliwość trzeciego sygnału (Hz)

signal = 0.5 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.sin(2 * np.pi * f2 * t) + 0.2 * np.sin(2 * np.pi * f3 * t)

# Obliczenie szybkiej transformaty Fouriera (FFT)
signal_fft = np.fft.fft(signal)
signal_freq = np.fft.fftfreq(len(signal), T)

# Funkcja do obliczania dyskretnej transformaty Fouriera (DFT)
def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Obliczenie DFT
signal_dft = dft(signal)

# Wizualizacja wyników
plt.figure(figsize=(12, 7))

# Oryginalny sygnał
plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title("Oryginalny sygnał")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

# Transformata Fouriera (FFT)
plt.subplot(3, 1, 2)
plt.plot(signal_freq[:len(signal)//2], np.abs(signal_fft)[:len(signal)//2] * 1 / len(signal))
plt.title("Szybka transformata Fouriera (FFT)")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")

# Dyskretna transformata Fouriera (DFT)
plt.subplot(3, 1, 3)
plt.plot(signal_freq[:len(signal)//2], np.abs(signal_dft)[:len(signal)//2] * 1 / len(signal))
plt.title("Dyskretna transformata Fouriera (DFT)")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")

plt.tight_layout()
plt.show()

#Zad 61
import numpy as np
from scipy.io.wavfile import write

def savewave(filename, s, fs=44100):
    # Normalizacja sygnału do zakresu -1 do 1
    s = s / np.max(np.abs(s))
    # Konwersja do 16-bitowego formatu PCM
    s = np.int16(s * 32767)
    # Zapis do pliku
    write(filename, fs, s)

def soundsec(duration, fs=44100):
    return np.linspace(0, duration, int(fs * duration), endpoint=False)

# Parametry
fs = 44100  # Częstotliwość próbkowania
duration1 = 1  # Czas trwania pierwszej części sygnału (w sekundach)
duration2 = 1  # Czas trwania drugiej części sygnału (w sekundach)

# Czas trwania sygnałów
t1 = soundsec(duration1, fs)
t2 = soundsec(duration2, fs)

# Generowanie sygnałów
signal_440Hz = np.sin(2 * np.pi * 440 * t1)
signal_220Hz = 0.5 * np.sin(2 * np.pi * 220 * t1)
signal_880Hz = 0.5 * np.sin(2 * np.pi * 880 * t1)
signal_330Hz = np.sin(2 * np.pi * 330 * t2)

# Sumowanie sygnałów w pierwszej sekundzie
combined_signal_first_part = signal_440Hz + signal_220Hz + signal_880Hz

# Łączenie obu części sygnału
combined_signal = np.concatenate((combined_signal_first_part, signal_330Hz))

# Zapis sygnału do pliku
savewave('dzwiek1.wav', combined_signal)

#Zad 62
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import librosa
import librosa.display

def savewave(filename, s, fs=44100):
    s = s / np.max(np.abs(s))
    s = np.int16(s * 32767)
    write(filename, fs, s)

def soundsec(duration, fs=44100):
    return np.linspace(0, duration, int(fs * duration), endpoint=False)

fs = 44100
duration1 = 1
duration2 = 1

t1 = soundsec(duration1, fs)
t2 = soundsec(duration2, fs)

signal_440Hz = np.sin(2 * np.pi * 440 * t1)
signal_220Hz = 0.5 * np.sin(2 * np.pi * 220 * t1)
signal_880Hz = 0.5 * np.sin(2 * np.pi * 880 * t1)
signal_330Hz = np.sin(2 * np.pi * 330 * t2)

combined_signal_first_part = signal_440Hz + signal_220Hz + signal_880Hz
combined_signal = np.concatenate((combined_signal_first_part, signal_330Hz))

savewave('dzwiek1.wav', combined_signal)


from scipy.io import wavfile

# Wczytaj plik dźwiękowy
fs, y = wavfile.read('dzwiek1.wav')

# Konwertuj dane audio na format zmiennoprzecinkowy
y = y.astype(np.float32)

# Wyświetl podstawowe informacje o pliku
print(f"Częstotliwość próbkowania: {fs} Hz")
print(f"Liczba próbek: {len(y)}")
print(f"Czas trwania: {len(y) / fs} sekundy")

# Analiza widmowa
def analyze(y, fs, fmin, fmax, rate, points):
    plt.figure(figsize=(14, 5))
    S = librosa.stft(y, n_fft=points)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
    librosa.display.specshow(S_db, sr=fs, x_axis='time', y_axis='log', fmin=fmin, fmax=fmax)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spektrogram')
    plt.show()

# Parametry analizy
fmin = 20
fmax = 2000
rate = 44100
points = 2048

analyze(y, fs, fmin, fmax, rate, points)

#Zad63

#a
import numpy as np
import matplotlib.pyplot as plt

def generate_signal(frequency, duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal

# Parametry sygnału
frequency = 1000  # 1 kHz
duration = 0.01  # 10 ms
fs1 = 44100  # Częstotliwość próbkowania 44.1 kHz
fs2 = 11025  # Częstotliwość próbkowania 11.025 kHz

# Generowanie sygnałów
t1, signal1 = generate_signal(frequency, duration, fs1)
t2, signal2 = generate_signal(frequency, duration, fs2)

# Wykres sygnałów
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t1, signal1, label='44100 Hz')
plt.title('Sygnał próbkowany z częstotliwością 44100 Hz')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t2, signal2, label='11025 Hz')
plt.title('Sygnał próbkowany z częstotliwością 11025 Hz')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
#b
# Parametry sygnału
frequency_high = 6000  # 6 kHz
duration = 0.01  # 10 ms
fs1 = 44100  # Częstotliwość próbkowania 44.1 kHz
fs2 = 11025  # Częstotliwość próbkowania 11.025 kHz

# Generowanie sygnałów
t1_high, signal1_high = generate_signal(frequency_high, duration, fs1)
t2_high, signal2_high = generate_signal(frequency_high, duration, fs2)

# Wykres sygnałów
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t1_high, signal1_high, label='44100 Hz')
plt.title('Sygnał 6 kHz próbkowany z częstotliwością 44100 Hz')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t2_high, signal2_high, label='11025 Hz')
plt.title('Sygnał 6 kHz próbkowany z częstotliwością 11025 Hz')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
#C
def quantize_signal(signal, num_bits):
    max_val = 2**(num_bits - 1) - 1
    min_val = -2**(num_bits - 1)
    quantized_signal = np.round(signal * max_val)
    quantized_signal = np.clip(quantized_signal, min_val, max_val)
    quantized_signal = quantized_signal / max_val
    return quantized_signal

# Parametry sygnału
frequency = 1000  # 1 kHz
duration = 0.01  # 10 ms
fs = 44100  # Częstotliwość próbkowania 44.1 kHz

# Generowanie sygnału
t, signal = generate_signal(frequency, duration, fs)

# Kwantowanie sygnału
signal_16bit = signal  # 16-bitowy sygnał oryginalny
signal_4bit = quantize_signal(signal, 4)

# Wykres sygnałów
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal_16bit, label='16 bit')
plt.title('Sygnał 16-bitowy')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, signal_4bit, label='4 bit')
plt.title('Sygnał 4-bitowy')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
