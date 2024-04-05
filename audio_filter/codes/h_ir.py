import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
h = np.loadtxt('values.dat')[1]
n = range(len(h))

plt.stem(n, h)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')

plt.savefig('../figs/h_n.png')

y = np.convolve(x, h)
n = np.arange(0, len(y))

plt.clf()
plt.stem(n, y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')

plt.savefig('../figs/conv_y.png')

