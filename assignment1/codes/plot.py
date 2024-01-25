import numpy as np
import matplotlib.pyplot as plt 

# only odd N
# even N non-symmetric output
N = 13

# make a sequence of numbers from -N//2 to N//2 (for odd N)
# and cast to float32 type
seq = (np.arange(-4, N, 1)).astype(np.float32)

# a_n GP
GP_A = 2 * np.power(2.0 ** 0.5, seq) * np.heaviside(seq, 1)

plt.stem(seq, GP_A, 'ro', basefmt='k')
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
GP_B = 3.0 ** 0.5 * np.power(3.0 ** 0.5, seq) * np.heaviside(seq, 1)

plt.stem(seq, GP_B, 'go', basefmt='k')
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
GP_C = np.power(1 / 3.0, seq) * np.heaviside(seq, 1) / 3.0

plt.stem(seq, GP_C, 'bo', basefmt='k')
plt.stem([8], [1/19683], 'mo', basefmt='k', label='$x_3(k_3)$')
plt.xlabel('n')
plt.ylabel('$x_3$(n)')
plt.grid()
plt.legend(fontsize='16')
# save plot
plt.savefig('figs/c.png')
