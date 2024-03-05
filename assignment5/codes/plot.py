import numpy as np
import matplotlib.pyplot as plt 

values = np.loadtxt('codes/values.txt', delimiter=' ')

# a_n GP
plt.plot(values[0], values[1], 'r')
plt.stem([37.5, 62.5, 137.5, 162.5], [3] * 4, 'r', basefmt=' ')
plt.xlabel('$\omega$')
plt.ylabel('$\\left\\vert{X_s(j\omega)}\\right\\vert$')
plt.grid()
# save plot
plt.savefig('figs/X_s.png')
