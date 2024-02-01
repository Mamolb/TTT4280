import numpy as np 
import matplotlib.pyplot as plt

#Want to calculate the relative uncertainty of the function f 

#We have two variables tau and d, with relative unifrom uncertainty of 

nrand = 1000
tauvec = (1 + 2*0.01*(np.random.rand(nrand) - 0.5))
dvec = (1 + 2*0.02*(np.random.rand(nrand) - 0.5))

#We want to calculate the relative uncertainty of the function f = c*tau/d
#Where c has no uncertainty

c = 300000000
f = c*tauvec/dvec

f_max = np.max(f)
f_min = np.min(f)

relative_MaxValue = np.abs(f_max/c-1)
relative_MinValue = np.abs(f_min/c-1)

if relative_MaxValue > relative_MinValue:
    relative_uncertainty = np.round(relative_MaxValue,4)
else:
    relative_uncertainty = np.round(relative_MinValue,4)

print("The max value is: ", relative_MaxValue)
print("The min value is: ", relative_MinValue)
print("The relative uncertainty is: ", relative_uncertainty)

