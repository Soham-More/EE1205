import numpy as np
import matplotlib.pyplot as plt

h = np.loadtxt('values.dat')[1]
N = len(h)

x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x.resize(N)

X = np.fft.fft(x)
H = np.fft.fft(h)
Y = X * H

y_alt = np.fft.ifft(Y)

print('X(k) =', X)
print('H(k) =', H)
print('Y(k) = X(k)H(k) =', Y)
print('y(n) =', np.abs(y_alt))

def DFT(x):
    n = np.arange(0, len(x), dtype=np.float64)
    X = [np.sum(x * np.exp(-2j * np.pi * n * k / len(x))) for k in range(len(x))]
    return np.array(X)

def IDFT(x):
    n = np.arange(0, len(x), dtype=np.float64)
    X = [np.sum(x * np.exp(2j * np.pi * n * k / len(x))) for k in range(len(x))]
    return np.array(X) / len(x)

Y_DFT = DFT(x) * DFT(h)
y_dft = IDFT(Y_DFT)

n = np.arange(N)

plt.stem(n, np.abs(y_alt), 'ro', label='FFT y(n)')
plt.stem(n, np.abs(y_dft), 'bo', label='DFT y(n)')
plt.legend()
plt.savefig('../figs/ft_comp.png')

