import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal

#read .wav file 
input_signal,fs = sf.read('../audio/alt.wav') 

#sampling frequency of Input signal
sampl_freq=fs

#order of the filter
order=4

#cutoff frquency 4kHz
cutoff_freq=2.0

#digital frequency
Wn=2*cutoff_freq/sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order,Wn, 'low')

#filter the input signal with butterworth filter
#Specify axis, since input is stereo
output_signal = signal.filtfilt(b, a, input_signal, axis=0)
#output_signal = signal.lfilter(b, a, input_signal)

def lfilt(b, a, x):
    y = []

    for n in range(len(x)):
        y_n = b[0]*x[n]

        for k in range(1, min(len(x) + 1, len(b), n + 1)):
            y_n += b[k]*x[n-k]
        for k in range(1, min(len(y) + 1, len(a))):
            y_n -= a[k]*y[-k]
        y_n = y_n / a[0]
        y.append(y_n)

    return np.array(y)

def filtfilt(b, a, x):
    # Apply 'odd' padding to input signal
    padding_length = 3 * max(len(a), len(b))  # the scipy.signal.filtfilt default
    x_forward = np.concatenate((
        [2 * x[0] - xi for xi in x[padding_length:0:-1]],
        x,
        [2 * x[-1] - xi for xi in x[-2:-padding_length-2:-1]]))

    y = lfilt(b, a, x_forward)
    y = lfilt(b, a, y[::-1])

    return y[-padding_length-1:padding_length-1:-1]

out_sig = filtfilt(b, a, input_signal)

n = np.arange(len(output_signal))

#plt.stem(n, output_signal[:,0], label='numpy lfilter')
#plt.stem(n, out_sig[:,0], label='custom lfilter')
plt.plot(n, output_signal, 'r', label='scipy lfilter')
plt.plot(n, out_sig, 'b', label='custom lfilter')
plt.legend()

plt.savefig('../figs/lfilter.png')

