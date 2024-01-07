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
plt.stem(seq, getGPsequence(2, 2.0 ** 0.5), 'ro')
plt.xlabel('n')
plt.ylabel('$x_a$(n)')
plt.title('$x_a$(n) plot')
plt.grid()
# save plot
plt.savefig('figs/a.png')

# clear previous plot
plt.clf()
# b_n GP
plt.stem(seq, getGPsequence(3.0 ** 0.5, 3.0 ** 0.5), 'go')
plt.xlabel('n')
plt.ylabel('$x_b$(n)')
plt.title('$x_b$(n) plot')
plt.grid()
# save plot
plt.savefig('figs/b.png')

# clear previous plot
plt.clf()
# c_n GP
plt.stem(seq, getGPsequence(1/3, 1/3), 'bo')
plt.xlabel('n')
plt.ylabel('$x_c$(n)')
plt.title('$x_c$(n) plot')
plt.grid()
# save plot
plt.savefig('figs/c.png')
