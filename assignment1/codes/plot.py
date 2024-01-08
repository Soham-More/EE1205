import numpy as np
import matplotlib.pyplot as plt 

# only odd N
# even N non-symmetric output
N = 13

# make a sequence of numbers from -N//2 to N//2 (for odd N)
# and cast to float32 type
seq = (np.arange(N) - N//2).astype(np.float32)

# construct a GP sequence
def getGPsequence(a, r):
    GP = a * np.power(r, seq) * np.heaviside(seq, 1)
    return GP

# a_n GP
plt.stem(seq, getGPsequence(2, 2.0 ** 0.5), 'ro', basefmt='k')
plt.xlabel('n')
plt.ylabel('$x_1$(n)')
plt.title('$x_1$(n) plot')
plt.grid()
# save plot
plt.savefig('figs/a.png')

# clear previous plot
plt.clf()
# b_n GP
plt.stem(seq, getGPsequence(3.0 ** 0.5, 3.0 ** 0.5), 'go', basefmt='k')
plt.xlabel('n')
plt.ylabel('$x_2$(n)')
plt.title('$x_2$(n) plot')
plt.grid()
# save plot
plt.savefig('figs/b.png')

# clear previous plot
plt.clf()
# c_n GP
plt.stem(seq, getGPsequence(1/3, 1/3), 'bo', basefmt='k')
plt.xlabel('n')
plt.ylabel('$x_3$(n)')
plt.title('$x_3$(n) plot')
plt.grid()
# save plot
plt.savefig('figs/c.png')
