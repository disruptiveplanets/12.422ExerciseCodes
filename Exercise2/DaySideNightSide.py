import numpy as np
import matplotlib.pyplot as plt

#Defining constants
G = 6.672e-11 # m^3 kg^-1 s^-2, courtesy Wikipedia
c = 299792458 # m s^-1, courtesy Wikipedia
h = 6.626e-34 # J s, courtesy Wikipedia
boltzmann = 1.38e-23 # J K^-1, courtesy Wikipedia


def planck(L,T):
    '''
    L: Wavelength in microns
    T: Temperature in Kelvin

    Returns:
      Array of spectral density in a given wavelength and a temperature
    '''
    L = L*1e-6 #convert microns to meters
    return 2.*h*(c**2.)/(L**5.)/np.expm1(h*c/(L*boltzmann*T))


#Complete the following code

#possible range of temperature for planets
Temps_Planet = np.logspace(2,4,1000)  #Goes from 100K to 10000K
Temp_Star = 5023
Rp_Rs = 0.1504

#Please fill in the following line of code
FluxStar = planck(??, Temp_Star)
FluxPlanet = planck(??, Temps_Planet)


#Why do we multiply by 1e6
FluxRatio = FluxPlanet/FluxStar*(Rp_Rs)**2*1e6



#Now let us plot flux as function of temperature
plt.figure(figsize=(12,8))
plt.plot(Temps_Planet, FluxRatio, "ko")
plt.axhline(y=3400-1100, color="red")
plt.axhline(y=3400, color="green")
plt.xlabel("Temperature of planet")
plt.ylabel("Flux ratio between planet/star")
plt.show()


#Automatically find where the line are intersecting
Index1 = np.argmin(np.abs(FluxRatio-3400))
Index2 = np.argmin(np.abs(FluxRatio-(3400-1100)))

print("The first temperature is:", Temps_Planet[Index1])
print("The second temperature is:", Temps_Planet[Index2])
