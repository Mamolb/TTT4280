#Task 4

#Same but with window-function

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
#Create a window function. We use the Hanning window
windowFunction = np.hanning(NumberOfSamples+1)
#Multiply the signal with the window function
windoSignal = signal*windowFunction
#Calculate the FFT of the signal
numberOfFFTSamples = 4096
#Frequency axis
frequency_step = samplingRate/numberOfFFTSamples
frequency_axis = np.fft.fftfreq(numberOfFFTSamples)
fftSignal = np.fft.fft(signal,numberOfFFTSamples)
windowFFTSignal = np.fft.fft(windoSignal,numberOfFFTSamples)
#Convert to dB
PowerSpectrum = np.abs(fftSignal)**2
windowPowerSpectrum = np.abs(windowFFTSignal)**2
newFrequencyAxis = np.linspace(0,5000,numberOfFFTSamples)
# Calculate Power Spectrum and Convert to dB and normalize
PowerSpectrum_dB = 20 * np.log10(np.abs(fftSignal) / np.sqrt(numberOfFFTSamples))
PowerSpectrum_dB = PowerSpectrum_dB - max(PowerSpectrum_dB)
#Nomalize the window-signal
windowPowerSpectrum_dB = 20 * np.log10(np.abs(windowFFTSignal) / np.sqrt(numberOfFFTSamples))
windowPowerSpectrum_dB = windowPowerSpectrum_dB - max(windowPowerSpectrum_dB)

#Plot the signal on each other
plt.plot(newFrequencyAxis[:numberOfFFTSamples // 4], PowerSpectrum_dB[:numberOfFFTSamples // 4], label='FFT of signal')
plt.plot(newFrequencyAxis[:numberOfFFTSamples // 4], windowPowerSpectrum_dB[:numberOfFFTSamples // 4], label='FFT of signal with window')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Relative Power [dB]')
plt.title('Power Spectral Density of the Signal with and without window')
plt.grid(True)
plt.ylim(-80, 10)  # Set y-axis limits
plt.legend()
plt.show()

#As we can see using a Hanning-window function we get a lot less side lobes. This however comes at a price
#of a broder main lobe. This can make it harder to distinguish between frequencies close to each other. 
#This is a trade-off that we have to make. We can also observe that the amplitude of the windowed signal is smoother. 
#This is because the signal is less affected by the abrupt start and end points,

