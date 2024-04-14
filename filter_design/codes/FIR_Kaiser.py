import numpy as np
import matplotlib.pyplot as plt
import values

# Define the range of 'n'
n = np.arange(-1000, 1001)

# Calculate the values of h_lp(n)
h_lp = np.where((n != 0) & (n >= -48) & (n <= 48), np.sin(n * np.pi / 40) / (n * np.pi), 0)

# Compute the Discrete Fourier Transform (DFT) of h_lp(n)
h_lp_fft = np.fft.fftshift(np.fft.fft(h_lp))

# Define the frequency axis with respect to omega/pi
N = len(n)
freq = np.fft.fftshift(np.fft.fftfreq(N)) * 2 * np.pi

# Plot the frequency spectrum for w/pi between -0.3 and 0.3
plt.plot(freq / np.pi, np.abs(h_lp_fft))
plt.xlabel('$\\frac{\\omega}{\\pi}$')
plt.ylabel('$|H_{lp}(\\omega)|$')
plt.title("FIR lowpass filter")
plt.xlim(-0.7, 0.7)
plt.grid(True)
plt.savefig("../figs/FIR_kaiser_lp.png")

plt.clf()

# Calculate the values of h_lp(n)
h_bp = np.where((n != 0) & (n >= -48) & (n <= 48), 2 * np.sin(n * np.pi / 40) * np.cos(n * 0.365 * np.pi) / (n * np.pi), 0)

# Compute the Discrete Fourier Transform (DFT) of h_lp(n)
h_bp_fft = np.fft.fftshift(np.fft.fft(h_bp))

# Define the frequency axis with respect to omega/pi
N = len(n)
freq = np.fft.fftshift(np.fft.fftfreq(N)) * 2 * np.pi

# Plot the frequency spectrum for w/pi between -0.3 and 0.3
plt.plot(freq / np.pi, np.abs(h_bp_fft))
plt.xlabel('$\\frac{\\omega}{\\pi}$')
plt.ylabel('$|H_{bp}(\\omega)|$')
plt.title("FIR bandpass filter")
plt.xlim(-0.7, 0.7)
plt.grid(True)
plt.savefig("../figs/FIR_kaiser_bp.png")