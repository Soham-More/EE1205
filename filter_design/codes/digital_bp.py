import numpy as np
import matplotlib.pyplot as plt
import sympy
import values

# simplify

z = sympy.Symbol('z')
substitution = ((1 - z**-1) / (1 + z**-1))

# analog filter
H_ABP = values.H_BP_symbolic / values.H_BP_numerator_coeff

# digital filter
H_DBP = H_ABP.subs(values.S, substitution)
H_DBP = sympy.simplify(H_DBP)

n, d = sympy.fraction(H_DBP)

print('H_dBP(z) numerator   = ', ' + '.join([f'{n.coeff(z, k):.3f}z^{{{-k}}}' for k in range(sympy.degree(n)+1)]))
print('H_dBP(z) denominator = ', ' + '.join([f'{d.coeff(z, k):.3f}z^{{{-k}}}' for k in range(sympy.degree(d)+1)]))

omega_s = sympy.Symbol('omega')
substitution = sympy.exp(1j * omega_s)
H_ZBP = H_DBP.subs(z, substitution)

omega = np.linspace(-np.pi/2, np.pi/2, 300)
H_values = [values.H_BP_numerator_coeff * np.abs(H_ZBP.evalf(subs={omega_s:i})) for i in omega]

plt.plot(omega/np.pi, H_values)
plt.xlabel('$\\frac{\\omega}{\\pi}$')
plt.ylabel('$|H_{dBP}(j\\Omega)|$')
plt.grid()
plt.savefig('../figs/digital_BP.png')

