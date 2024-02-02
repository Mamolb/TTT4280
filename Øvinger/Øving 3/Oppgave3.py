import numpy as np
import matplotlib.pyplot as plt

nrand = 100000
d = 0.1
c = 343.
thetas = np.radians(np.arange(1, 90))
dtau = 0.01
dd = 0.02
tau_nominal = np.cos(thetas)*d/c
ds = d*(1 + dd*2*(np.random.rand(nrand) - 0.5))
taus = tau_nominal*(1 + dtau*2*(np.random.rand(nrand, tau_nominal.shape[0]) - 0.5))
temps = c*taus.T/ds # Transpose necessary due to broadcasting rules
# Before applying arccos, ensure temps is within the valid range for arccos
temps_clipped = np.clip(temps, -1, 1)  # Clip values to be between -1 and 1
theta_estimates = np.arccos(temps_clipped)  # Now safe to call arccos
means = np.nanmean(theta_estimates, axis=-1)
maxes = np.nanmax(theta_estimates, axis=-1)
mins = np.nanmin(theta_estimates, axis=-1)
# Gives the errors relative to the means; causes bias!

# Use ‘thetas’ in place of ‘means’ to get unbiased errors
relative_max = maxes/means - 1
relative_min = mins/means - 1
fig = plt.figure()
ax = fig.gca()
h = ax.plot(np.degrees(thetas), np.degrees(np.vstack((thetas, means, maxes, mins)).T))
leg = ax.legend(("True $\\theta$", "Mean $\hat{\\theta}$",
"Max $\hat{\\theta}$", "Min $\hat{\\theta}$"))

ax.set_xlabel("Incidence Angle $\\theta$ (degrees)")
ax.set_ylabel("Estimated Incidence $\hat{\\theta}$ (degrees)")
fig = plt.figure()
ax = fig.gca()
h = ax.plot(np.degrees(thetas), np.vstack((relative_max, -relative_min)).T)
leg = ax.legend(("$|\hat{\\theta}_{max}-\\theta|$", "$|\hat{\\theta}_{min}-\\theta|$"))
ax.set_xlabel("$\\theta$ (degrees)")
ax.set_ylabel("Relative Error in Estimate")
plt.show()
# The relative error is not constant, but increases with the incidence angle
#The max value is 
print("The max value is: ", np.max(relative_max))
