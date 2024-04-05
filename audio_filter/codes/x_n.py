import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
n = range(len(x))

plt.stem(n, x)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')

plt.savefig('../figs/x_n.png')

y = np.loadtxt('values.dat')[0]
n = range(len(y))

plt.clf()
plt.stem(n, y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')

plt.savefig('../figs/y_n.png')

