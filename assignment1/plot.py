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
    GP = a * np.power(r, seq - 1) * np.heaviside(seq, 0)
    return GP

# a_n GP
plt.stem(seq, getGPsequence(2, 2.0 ** 0.5), 'ro', label='$x_a$(n)')
plt.stem(seq, getGPsequence(3.0 ** 0.5, 3.0 ** 0.5), 'go', label='$x_b$(n)')
plt.stem(seq, getGPsequence(1/3, 1/3), 'bo', label='$x_c$(n)')
plt.xlabel('n')
plt.ylabel('values')
plt.title('$x_a$(n), $x_b$(n), $x_c$(n) plot')
plt.grid()
plt.legend(['$x_a$(n)', '$x_b$(n)', '$x_c$(n)'])
# save plot
plt.savefig('figs/a.png')
