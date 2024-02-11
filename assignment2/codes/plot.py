import numpy as np
import matplotlib.pyplot as plt 

values = np.loadtxt('codes/values.txt', delimiter=' ')

# a_n GP
plt.plot(values[0], values[1], 'r')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.grid()
# save plot
plt.savefig('figs/x_t.png')
