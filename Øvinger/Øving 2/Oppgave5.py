#Same but with complex signal
import numpy as np
import matplotlib.pyplot as plt
#Definng some variables
f = 0
A = 1
samplingTime = 0.2*10**-3
samplingRate = 1/(samplingTime)

#Defining the time vector
NumberOfSamples = 900
t = np.linspace(0,NumberOfSamples*(samplingTime),NumberOfSamples+1)
#Defining the signal
complexSignal = A*np.exp(-1j*2*np.pi*f*t)
#We need to find the PSD of the signal.
#Calculate the FFT of the signal
numberOfFFTSamples = 4096
#Frequency axis
frequency_axis = np.fft.fftfreq(numberOfFFTSamples)
newFrequencyAxis = np.linspace(0,samplingRate,numberOfFFTSamples)
fftComplexSignal = np.fft.fft(complexSignal,numberOfFFTSamples)

# Calculate Power Spectrum and Convert to dB and normalize
PowerSpectrum_dB = 20 * np.log10(np.abs(fftComplexSignal) / np.sqrt(numberOfFFTSamples))
PowerSpectrum_dB = PowerSpectrum_dB - max(PowerSpectrum_dB)
#plot the signal up to its sampling rate
# plt.plot(newFrequencyAxis, PowerSpectrum_dB)
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Relartive Power [dB]')
# plt.title('Power Spectral Density of the complex signal')
# plt.grid(True)
# plt.show()

#We observe a peak at 4900 Hz. This is the alias of the signal at -100 Hz.
#This is because the signal is complex and not real. If we change the
#signal to complexSignal = A*np.exp(1j*2*np.pi*f*t) we get a REAL frequency
#that peaks at 100Hz.

#Task 5b)

#I have changed the frequency to 0 Hz
X_f_shitfted = np.fft.fftshift(fftComplexSignal)
freq = np.fft.fftshift(frequency_axis)
#Plot the shifted signal
# plt.plot(freq, X_f_shitfted)
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Magnitude')
# plt.title('Power Spectral Density of the complex signal shifted')
# plt.grid(True)
# plt.show()

#Task 5c)
f = 100
A = 1
samplingTime = 0.2*10**-3
samplingRate = 1/(samplingTime)

#Defining the time vector
NumberOfSamples = 900
t = np.linspace(0,NumberOfSamples*(samplingTime),NumberOfSamples+1)
#Defining the signal
complexSignal = A*np.exp(1j*2*np.pi*f*t)
#We need to find the PSD of the signal.
#Calculate the FFT of the signal
numberOfFFTSamples = 4096
#Frequency axis
frequency_axis = np.fft.fftfreq(numberOfFFTSamples)
newFrequencyAxis = np.linspace(0,samplingRate,numberOfFFTSamples)
fftComplexSignal = np.fft.fft(complexSignal,numberOfFFTSamples)

# Calculate Power Spectrum and Convert to dB and normalize
PowerSpectrum_dB = 20 * np.log10(np.abs(fftComplexSignal) / np.sqrt(numberOfFFTSamples))
PowerSpectrum_dB = PowerSpectrum_dB - max(PowerSpectrum_dB)

#plot the signal up to its sampling rate
plt.plot(newFrequencyAxis, PowerSpectrum_dB)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Relartive Power [dB]')
plt.title('Power Spectral Density of the complex signal with positive value')
plt.grid(True)
plt.show()

#Here we observe a peak at 100 Hz. This is because the signal now has a real frequency.
