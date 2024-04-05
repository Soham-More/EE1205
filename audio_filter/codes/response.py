import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

a = [ 1.0, -1.96842779,1.73586071,-0.72447083,0.1203896 ]
b = [0.01020948,0.04083792,0.06125688,0.04083792,0.01020948]

sampl_freq = 48000
T = 1/sampl_freq

w = np.linspace(10000, 100000, 10000)
z = np.exp(-1j*w*T)

response = np.abs(poly.polyval(z**-1, b) / poly.polyval(z**-1, a))

plt.plot(np.log10(w), response)
plt.xlabel('$log_{10}(\\omega)$')
plt.ylabel('$|H(e^{j\\omega})|$')
plt.savefig('../figs/freq_res.png')


