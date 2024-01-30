#Task 2
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
numberOfFFTSamples = 1024
#Frequency axis
frequency_step = samplingRate/numberOfFFTSamples
frequency_axis = np.fft.fftfreq(numberOfFFTSamples,samplingTime)
fftSignal = np.fft.fft(signal,numberOfFFTSamples)
#Convert to dB
ffTDesibelSignal = 20*np.log10(np.abs(fftSignal))

#BLIR MEGA STYGG NÅR JEG PLOTTER FREKVENS MED DB VET IKKE HVORFOR?

#Task 2 b)
PowerSpectrum = np.abs(fftSignal)**2
newFrequencyAxis = np.linspace(0,5000,numberOfFFTSamples)
#plotting the signal
# plt.plot(newFrequencyAxis,PowerSpectrum)
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Amplitude of X(f)')
# plt.title('Plot of periodogram of Jean Joseph´s signal')
# plt.grid(True)
# plt.show()

#Task 2 c)
#Only plot from 0 to 200 Hz
samplesTo200Hz = int(200/frequency_step)
#plt.plot(newFrequencyAxis[0:samplesTo200Hz],X_f[0:samplesTo200Hz])
#plt.show()

#Task 2 d)

# Calculate Power Spectrum and Convert to dB and normalize
PowerSpectrum_dB = 20 * np.log10(np.abs(fftSignal) / np.sqrt(numberOfFFTSamples))
PowerSpectrum_dB = PowerSpectrum_dB - max(PowerSpectrum_dB)

# Plot the signal

plt.plot(frequency_axis[:numberOfFFTSamples // 2], PowerSpectrum_dB[:numberOfFFTSamples // 2])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Relative Power [dB]')
plt.title('Power Spectral Density of the Signal')
plt.grid(True)
plt.ylim(-80, 10)  # Set y-axis limits
plt.show()