import soundfile as sf
from scipy import signal

#read .wav file 
input_signal,fs = sf.read('../audio/alt.wav') 

#sampling frequency of Input signal
sampl_freq=fs

print(fs)

#order of the filter
order=4   

#cutoff frquency 4kHz
cutoff_freq=6000.0

#digital frequency
Wn=2*cutoff_freq/sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order,Wn, 'low')

print('a =', a)
print('b =', b)

#filter the input signal with butterworth filter
#Specify axis, since input is stereo
output_signal = signal.filtfilt(b, a, input_signal, axis=0)
#output_signal = signal.lfilter(b, a, input_signal)

#write the output signal into .wav file
sf.write('../audio/alt_filtered.wav', output_signal, fs) 
