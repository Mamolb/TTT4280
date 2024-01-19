#Excersise 1 for TTT4280

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng


def continuous_uniform_distribution(x, low=4950, high=5050):
    return np.where((low <= x) & (x <= high), 1, 0)


#1.1
#Find the mean value and standard deviation of the data set
data = np.loadtxt('Øving 1/data.txt', delimiter=',')
newData = np.loadtxt('Øving 1/newdata.txt', delimiter=',')
meanDataValue = data.mean()
stdDataValue = data.std()
#1.2c
#Caclculate for half the data set
halfData = data[:int(len(data)/2)]
meanHalfDataValue = halfData.mean()
stdHalfDataValue = halfData.std()

#1.3c

# Example usage
x_values = np.linspace(4900, 5100, 1000)  # Generate 1000 points from 4900 to 5100
y_values = continuous_uniform_distribution(x_values)

# Convolve the distribution with itself
convolved = np.convolve(y_values, y_values, mode='full')

# Generate new x values for the convolved function
convolved_x_values = np.linspace(2*x_values[0], 2*x_values[-1], len(convolved))

# Plot the convolved function
plt.plot(convolved_x_values, convolved)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Convolved function of two uniform distributions')
plt.show()

#1.4c
rng = default_rng()
delta_r = 100

resistor = 5000
deviationToResitor = resistor * 0.01

totaleValues = 6000

Rvalue1 = resistor +2*deviationToResitor*(rng.random(totaleValues)-0.5)
Rvalue2 = resistor +2*deviationToResitor*(rng.random(totaleValues)-0.5)

r_values = Rvalue1 + Rvalue2
#Find the relative standard deviation
RelativeStandardDeviation = r_values.std()/r_values.mean()*100
print("Relative standard deviation: ", RelativeStandardDeviation)


'''
print("Mean value half: ", meanHalfDataValue)
print("Standard deviation half: ", stdHalfDataValue)


print("Mean value: ", meanDataValue)
print("Standard deviation: ", stdDataValue)
'''