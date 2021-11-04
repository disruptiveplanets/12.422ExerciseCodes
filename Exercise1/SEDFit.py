import numpy as np
import matplotlib.pyplot as plt
from Functions import ConvertMag2Flux, planckCGS
#SED Data for HD 189733 b
#https://exofop.ipac.caltech.edu/tess/target.php?id=256364928

#Constants
parsec = 3.086e18          #CGS
SolarRad = 6.9634e10       #CGS
c = 29979245800            #Speed of light in c

#Dictionary of values
Magnitude={'B':(8.607,0.02),
	       'V': (7.67,0.03),
           'J': (6.073,0.032),
	       'H': (5.587,0.031),
	       'K': (5.541,0.021)}


Band, WaveLength, WaveLengthRange, StellarFlux, \
StellarFluxError, StellarFluxDensity, \
StellarFluxDensityError = ConvertMag2Flux(Magnitude)

#Distance and the radius of the star
Distance = 19.7638*parsec
Radius = 0.886*SolarRad


WavelengthModel = np.linspace(0.3,3,1000) #in microns
WavelengthModelCM = WavelengthModel*1e-4  #in cm
Frequency = c/WavelengthModelCM

Factor =Radius**2/Distance**2
print("Factor::", Factor)


#Try different temperatures
Model1 = planckCGS(5700, WavelengthModelCM)*Factor*Frequency


plt.figure(figsize=(12,8))
plt.errorbar(WaveLength, StellarFlux, xerr=WaveLengthRange, yerr=StellarFluxError, marker="o", linestyle="None", capsize=3, color="black")
plt.plot(WavelengthModel,Model1, "r-")
plt.xlabel("Wavelength (microns)", fontsize=20)
plt.ylabel("Flux (ergs/s/cm^2)", fontsize=20)
plt.show()
