import numpy as np
import matplotlib.pyplot as plt 

values = np.loadtxt('codes/values.txt', delimiter=' ')

# a_n GP
plt.plot(values[0], values[1], 'r')
plt.xlabel('s')
plt.ylabel('$X(s)$')
plt.grid()
# save plot
plt.savefig('figs/X_s.png')
