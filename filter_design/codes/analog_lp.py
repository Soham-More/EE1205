import numpy as np
import matplotlib.pyplot as plt
import values

omega = np.linspace(0.0, 2.0, 50)

plt.plot(omega, np.abs(values.H_LP(1j * omega)), c='black', label='Design')
plt.scatter(omega, values.lowPassGain(values.epsilon, values.N, omega), c='r', marker='x', label='Specification')
plt.xlabel('$\\Omega_L$')
plt.ylabel('$|H_{aLP}(j\\Omega_L)|$')
plt.legend()
plt.grid()
plt.savefig('../figs/spec.png')
