import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

a = [ 1.0, -1.96842779,1.73586071,-0.72447083,0.1203896 ]
b = [0.01020948,0.04083792,0.06125688,0.04083792,0.01020948]

# calculates partial fraction residues, poles and polynomial terms
p = np.polynomial.polynomial.polyroots(a)
r = np.polynomial.polynomial.polyroots(b)

plt.scatter(p.real, p.imag, c='r')
plt.scatter(r.real, r.imag, c='b')
plt.grid()
plt.savefig('../figs/pole.png')

