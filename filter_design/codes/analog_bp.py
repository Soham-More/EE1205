import numpy as np
import matplotlib.pyplot as plt
import values

omega = np.linspace(-2.0, 2.0, 500)

plt.plot(omega, np.abs(values.H_BP(1j * omega)))
plt.xlabel('$\\Omega$')
plt.ylabel('$|H_{aBP}(j\\Omega)|$')
plt.grid()
plt.savefig('../figs/H_BP.png')

