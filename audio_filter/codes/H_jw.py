import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(-3 * np.pi, 3 * np.pi, 500)
H_jw = 4 * np.abs(np.cos(omega)) / np.sqrt(5.0 + 4.0 * np.cos(omega))

plt.plot(omega, H_jw)
plt.ylabel('$\\left|H(e^{j\\omega})\\right|$')
plt.xlabel('$\omega$')
plt.savefig('../figs/H_jw.png')

n = np.arange(-5, 15, dtype=np.float64)
h_n = np.power(-0.5, n)*np.heaviside(n, 1.0) + np.power(-0.5, n - 2)*np.heaviside(n - 2, 1.0)

plt.clf()
plt.stem(n, h_n)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.savefig('../figs/h_n.png')
