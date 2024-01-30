#Task 3

#Same as before but add zero-padding to the FFT. Make length 4096.

import numpy as np
import matplotlib.pyplot as plt
#Definng some variables
f = 100
A = 1
samplingTime = 0.2*10**-3
samplingRate = 1/(samplingTime)

#Defining the time vector
NumberOfSamples = 900
t = np.linspace(0,NumberOfSamples*(samplingTime),NumberOfSamples+1)
#Defining the signal
signal = A*np.sin(2*np.pi*f*t)
#Calculate the FFT of the signal
numberOfFFTSamples = 4096
#Frequency axis
frequency_step = samplingRate/numberOfFFTSamples
frequency_axis = np.fft.fftfreq(numberOfFFTSamples)
fftSignal = np.fft.fft(signal,numberOfFFTSamples)
#Convert to dB
ffTDesibelSignal = 20*np.log10(np.abs(fftSignal))

PowerSpectrum = np.abs(fftSignal)**2
newFrequencyAxis = np.linspace(0,5000,numberOfFFTSamples)
# Calculate Power Spectrum and Convert to dB and normalize
PowerSpectrum_dB = 20 * np.log10(np.abs(fftSignal) / np.sqrt(numberOfFFTSamples))
PowerSpectrum_dB = PowerSpectrum_dB - max(PowerSpectrum_dB)
#Normalize the windowed signal

# Plot the signal
plt.plot(newFrequencyAxis[:numberOfFFTSamples // 2], PowerSpectrum_dB[:numberOfFFTSamples // 2])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Relative Power [dB]')
plt.title('Power Spectral Density of the Signal with added zero-padding')
plt.grid(True)
plt.ylim(-80, 10)  # Set y-axis limits
plt.show()

#We can clearly see that when we change the length of the FFT we change the distance of the frequency-step. 
#This is even more clearer when we change to a length of 2*4096