import numpy as np
import matplotlib.pyplot as plt

h = np.loadtxt('values.dat')[1]
N = len(h)

def DFT(x):
    n = np.arange(0, len(x), dtype=np.float64)
    X = [np.sum(x * np.exp(-2j * np.pi * n * k / len(x))) for k in range(len(x))]
    return np.array(X)

def IDFT(x):
    n = np.arange(0, len(x), dtype=np.float64)
    X = [np.sum(x * np.exp(2j * np.pi * n * k / len(x))) for k in range(len(x))]
    return np.array(X) / len(x)

x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x.resize(N)

X = DFT(x)
H = DFT(h)
Y = DFT(x) * DFT(h)

y_alt = IDFT(Y)

print('X(k) =', X)
print('H(k) =', H)
print('Y(k) = X(k)H(k) =', Y)
print('y(n) =', np.abs(y_alt))
