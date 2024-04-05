import numpy as np
import matplotlib.pyplot as plt

value = np.loadtxt('time.dat')

plt.stem(np.power(2, value[:-1,0]), value[:-1,1], 'bo', label='FFT+IFFT execution')
plt.stem(np.power(2, value[:-1,0]), value[:-1,2], 'ro', label='Convolution execution')
plt.xlabel('Data size')
plt.ylabel('Time in seconds')
plt.legend()
plt.savefig('../figs/execplot.png')

