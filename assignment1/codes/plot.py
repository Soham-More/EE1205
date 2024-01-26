import numpy as np
import matplotlib.pyplot as plt 

values = np.loadtxt('codes/values.txt', delimiter=' ')

# a_n GP
plt.stem(values[0], values[1], 'ro', basefmt='k')
plt.stem([12], [128], 'mo', basefmt='k', label='$x_1(k_1)$')
plt.xlabel('n')
plt.ylabel('$x_1$(n)')
plt.grid()
plt.legend(fontsize='16')
# save plot
plt.savefig('figs/a.png')

# clear previous plot
plt.clf()

# b_n GP
plt.stem(values[0], values[2], 'go', basefmt='k')
plt.stem([11], [729], 'mo', basefmt='k', label='$x_2(k_2)$')
plt.xlabel('n')
plt.ylabel('$x_2$(n)')
plt.grid()
plt.legend(fontsize='16')
# save plot
plt.savefig('figs/b.png')

# clear previous plot
plt.clf()

# b_n GP
plt.stem(values[0], values[3], 'bo', basefmt='k')
plt.stem([8], [1/19683], 'mo', basefmt='k', label='$x_3(k_3)$')
plt.xlabel('n')
plt.ylabel('$x_3$(n)')
plt.grid()
plt.legend(fontsize='16')
# save plot
plt.savefig('figs/c.png')
