#Task 1 
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
#plotting the signal
#Just want to plot the first 200 values 
plt.figure(1)
plt.stem(t[0:200],signal[0:200])
plt.xlabel('Time [n]')
plt.ylabel('Amplitude')
plt.title('Discrete signal of a Jean Joseph´s signal') 
plt.grid(True)
plt.show()

