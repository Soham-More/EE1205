import numpy as np
import matplotlib.pyplot as plt
import values

epsilon_values = np.linspace(values.epsilon_bounds[0], values.epsilon_bounds[1], 4)
omega = np.linspace(0.0, 2.0, 100)

MaxCurve = np.zeros(omega.shape)
MinCurve = np.ones(omega.shape)

fig, ax = plt.subplots()

for epsilon in epsilon_values:
    gain_plot = values.lowPassGain(epsilon, values.N, omega)
    MaxCurve = np.maximum(gain_plot, MaxCurve)
    MinCurve = np.minimum(gain_plot, MinCurve)
    ax.plot(omega, values.lowPassGain(epsilon, values.N, omega), label=f'epsilon = {epsilon:.4f}')

ax.fill_between(omega, 1 - values.delta1, 1, where=omega < 1.0, alpha=0.5, label='Passband')
ax.fill_between(omega, 0.0, values.delta2, where=omega > values.W_lowpass_stop, alpha=0.5, label='Stopband')

ax.set_xlabel('$\\Omega_L$')
ax.set_ylabel('$|H_{aLP}(j\\Omega_L)|$')
ax.legend()
plt.savefig('../figs/epsilon_freq_res.png')

