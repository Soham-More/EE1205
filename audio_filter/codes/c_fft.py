import numpy as np
import ctypes

fftlib = ctypes.cdll.LoadLibrary('./fft.so')

N = 4
x = np.random.random(N).astype(np.float32)

# a wrapper for calling FFT from C
def fft_radix2(x):
    N = len(x)

    y_real = np.zeros(N, dtype=np.float32)
    y_imag = np.zeros(N, dtype=np.float32)

    fftlib.fft_radix2(ctypes.c_void_p(x.ctypes.data), ctypes.c_void_p(y_real.ctypes.data), ctypes.c_void_p(y_imag.ctypes.data), ctypes.c_size_t(N))

    return y_real + y_imag * 1j

print(x)
print(np.max(np.abs(fft_radix2(x) - np.fft.fft(x))))
