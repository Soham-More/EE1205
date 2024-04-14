import numpy as np
import matplotlib.pyplot as plt
import values

omega = np.linspace(-1.0, 1.0, 600)

B = values.w_pass[1] - values.w_pass[0]

plt.plot(omega, np.where(np.abs(omega) < B/2, 1.0, 0.0))
plt.scatter([B/2], [0.0], label='cutoff frequency', c='orange')
plt.xlabel('$\\omega$')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()
plt.title('Low Pass frequency response')
plt.savefig('../figs/FIR_ideal_w.png')

plt.clf()

n = np.arange(-100, 100, 2)
h_values = np.sin(B * n / 2)/(n * np.pi)
h_values[n == 0] = (B / 2)/(np.pi)

plt.stem(n, h_values)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.title('Impluse Response')    
plt.savefig('../figs/FIR_ideal_n.png')

n = np.arange(-100, 100, 2)
h_values = np.sin(B * n / 2)/(n * np.pi)
h_values[n == 0] = (B / 2)/(np.pi)

plt.stem(n, h_values)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.title('Impluse Response')    
plt.savefig('../figs/FIR_ideal_n.png')


