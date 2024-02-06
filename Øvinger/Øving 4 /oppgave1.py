import numpy as np
import matplotlib.pyplot as plt
#1.1
#Find the mean value and standard deviation of the data set
dataMed= np.loadtxt('Øvinger/Øving 4 /T60Med.txt', delimiter=',')
dataUten = np.loadtxt('Øvinger/Øving 4 /T60Uten.txt', delimiter=',')

V = 240
S_absorbent = 10
c = 343.4



estimteStandardDeviationMed = np.sqrt(1/(len(dataMed)-1) * np.sum((dataMed - dataMed.mean())**2))
print("Estimated standard deviation of dataMed: ", np.round(estimteStandardDeviationMed, 4))
estimateStandardDeviationUten = np.sqrt(1/(len(dataUten)-1) * np.sum((dataUten - dataUten.mean())**2))
print("Estimated standard deviation of dataUten: ", np.round(estimateStandardDeviationUten, 4))

alpha = (24*V*np.log(10) / (c*S_absorbent)) * (1/dataMed - 1/dataUten)
alphaMean = np.mean(alpha)

estimateStandardDeviationAlpha = ((24 * V * np.log(10)) / (c * S_absorbent))**2 * (((estimateStandardDeviationUten**2) / dataUten.mean()**4) + ((estimteStandardDeviationMed**2) / dataMed.mean()**4))
print("Estimated standard deviation of alpha: ", np.round(estimateStandardDeviationAlpha, 4))

#1.2
#Need to calculate a confidence interval for the alpha value

#From the web
t = 2.365

UpperalphaConfidenceInterval = alphaMean + t * estimateStandardDeviationAlpha/np.sqrt(len(alpha))
LoweralphaConfidenceInterval = alphaMean - t * estimateStandardDeviationAlpha/np.sqrt(len(alpha))

print("The confidence interval for alpha is: ", np.round(LoweralphaConfidenceInterval, 4), " to ", np.round(UpperalphaConfidenceInterval, 4))

