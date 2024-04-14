import numpy as np
import matplotlib.pyplot as plt
import values

poles = values.poles

plt.scatter(np.real(poles[np.real(poles) < 0.0]), np.imag(poles[np.real(poles) < 0.0]), marker='x')
plt.scatter(np.real(poles[np.real(poles) > 0.0]), np.imag(poles[np.real(poles) > 0.0]), marker='x')
plt.axis('equal')
plt.grid()
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.axvline(0.0, color=(0, 0, 0))
plt.axhline(0.0, color=(0, 0, 0))
plt.savefig('../figs/polezero.png')

