import numpy as np
import scipy.special
from sympy import Symbol, Poly
import sympy
import sympy.polys
import sympy.polys.polytools

def digitalToAnalog(digital_freq):
    return np.tan(digital_freq / 2)

roll_no = 11223 # roll no.
spec_sigma = sum(int(digit) for digit in str(roll_no)) # sigma
spec_j = (roll_no - 11000) % spec_sigma

kHz = 10 ** 3
F_s = 48 * kHz # 48 kHz sampling rate

f_pass = np.array([8.2 * kHz, 9.4 * kHz])
f_stop = np.array([7.9 * kHz, 9.7 * kHz])

delta1 = 0.15 # passband ripple 
delta2 = 0.15 # stopband ripple

# digital normalized angular passband edges frequency
w_pass = 2 * np.pi * f_pass / F_s
# digital normalized angular stopband edges frequency
w_stop = 2 * np.pi * f_stop / F_s

# analog normalized angular passband edges frequency
W_Pass = digitalToAnalog(w_pass)
# analog normalized angular stopband edges frequency
W_Stop = digitalToAnalog(w_stop)

W_0 = np.sqrt(W_Pass[0] * W_Pass[1]) # \Omega_0
B = W_Pass[1] - W_Pass[0]  # Bandwidth

D_1 = 1/((1 - delta1)**2) - 1
D_2 = 1/(delta2**2) - 1

def bandpassToLowpass(angular_freq):
    return (np.square(angular_freq) - (W_0**2)) * (1 / (B * angular_freq))

def bandpassToLowpass_s(s):
    return (np.square(s) + (W_0**2)) * (1 / (B * s))

# low pass filter stopband edge angular analog frequency
W_lowpass_stop = np.min(np.abs(bandpassToLowpass(W_Stop)))

N_min = np.ceil(np.arccosh(np.sqrt(D_2 / D_1)) / np.arccosh(W_lowpass_stop))

N = 4
epsilon = 0.3

def chebyshev(order, x):
    return scipy.special.eval_chebyt(order, x)

epsilon_bounds = np.array([ np.sqrt(D_2) / chebyshev(N, W_lowpass_stop), np.sqrt(D_1) ])

def lowPassGain(epsilon, order, x):
    return 1 / np.sqrt(1 + np.square(epsilon * chebyshev(order, x)))

poles = np.loadtxt('poles.dat', dtype=np.float64)
poles = poles[:,0] + 1j * poles[:,1]

negative_poles = poles[np.real(poles) < 0.0]

filter_denominator_coefficients = np.real(np.polynomial.polynomial.polyfromroots(negative_poles))

G_LP = np.abs(np.polynomial.polynomial.polyval(1j, filter_denominator_coefficients)) * lowPassGain(epsilon, N, 1)
G_BP = 1/np.abs(G_LP / np.polynomial.polynomial.polyval(1j, filter_denominator_coefficients))

def polyArrayToLatex(coeff, var):
    polynomial = [f'{coeff[k]:.3f}{var}^{k}' for k in range(len(coeff))]
    return ' + '.join(polynomial[::-1])

S = Symbol('s')

H_BP_denominator = sympy.simplify(sympy.compose(Poly.from_list(filter_denominator_coefficients[::-1], S), (S ** 2 + W_0**2) / (B*S)))
H_BP_denominator = sympy.simplify(H_BP_denominator*S**4)

H_BP_denominator_coeff = sympy.monic(H_BP_denominator).as_list()
H_BP_denominator_coeff = np.array([x[0] for x in H_BP_denominator_coeff])[::-1]
H_BP_numerator_coeff = G_BP * G_LP / sympy.LC(H_BP_denominator)

H_BP_symbolic = ((H_BP_numerator_coeff * S**4) / sympy.monic(H_BP_denominator))

def H_LP(s):
    return G_LP / np.polynomial.polynomial.polyval(s, filter_denominator_coefficients)

def H_BP(s):
    return (H_BP_numerator_coeff * s**4) / np.polynomial.polynomial.polyval(s, H_BP_denominator_coeff)

if __name__ == '__main__':
    print(f'{W_Pass=}')
    print(f'{W_Stop=}')
    print(f'{W_0=}')
    print(f'{B=}')
    print(f'{D_1=}')
    print(f'{D_2=}')
    print(f'{bandpassToLowpass(W_Stop)=}')
    print(f'{W_lowpass_stop=}')
    print(f'{N_min=}')
    print(f'{G_LP=}')
    print(f'{filter_denominator_coefficients=}')
    print(f'{polyArrayToLatex(filter_denominator_coefficients, "s_L")=}')
    print(f'{G_BP=}')
    print(f'{polyArrayToLatex(H_BP_denominator_coeff, "s")=}')
    print(f'{H_BP_numerator_coeff=}')


