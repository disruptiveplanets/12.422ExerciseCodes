#Code create by Prajwal Niraula for 12.422/12.622
#For manual using the hapi look at: https://hitran.org/static/hapi/hapi_manual.pdf

import hapi
import numpy as np
import matplotlib.pyplot as plt


#Create a grid of stopping wavelength
hapi.db_begin('data') #Load everything in the data website


#This is used to specify the temperature and pressure
#Environment={'p':1.0, 'T':296} p: bars, T: in Kelvins

#WavelengthGrid = np.arange(1,10, 0.001)
#Let's read the data
WavelengthGrid, ObsTransmivitty = np.loadtxt("TransmissivityData.txt", skiprows=1, unpack=True)

#Converting wavelenght to wavenumber. Wavenumber are often calculated in per cm. 
WaveNumberGrid = 1./WavelengthGrid[::-1]*1e4



#Let's check if the line position match up with the observed line position
#How does pressure change your transmissivity.

#Don't forget to download the data before you run the code below
nu_Voigt, coef_Voigt1 = hapi.absorptionCoefficient_Voigt(SourceTables='H2', Diluent={'air':1}, \
				Environment={'p':0.01, 'T':296}, OmegaGrid=WaveNumberGrid, HITRAN_units=False)

nu_Voigt, coef_Voigt2 = hapi.absorptionCoefficient_Voigt(SourceTables='H2', Diluent={'air':1}, \
				Environment={'p':0.01, 'T':296}, OmegaGrid=WaveNumberGrid, HITRAN_units=False)

#Maybe there is third component in the atmosphere
nu_Voigt, coef_Voigt3 = hapi.absorptionCoefficient_Voigt(SourceTables='H2', Diluent={'air':1}, \
				Environment={'p':0.01, 'T':296}, OmegaGrid=WaveNumberGrid, HITRAN_units=False)

#Add the 
coef_Voigt  = coef_Voigt1+coef_Voigt2#+coef_Voigt3
coef_Voigt = coef_Voigt[::-1]
#OmegaStep defines

####Hints
#1. Change the name of the molecule
#2. coeff_Voigt is in terms of per cm-1. So how do you convert that into optical depth, and how would you convert optical depth to transmissivity.

###Optical depth

#np.exp is fast way to evaluate exponent 
#CalcTransmissivity = ???







#This is for plotting purposes
plt.figure(figsize=(12,7))
plt.plot(WavelengthGrid, ObsTransmivitty, "r-",lw=3, alpha=0.4, label="Observed Data")
plt.plot(WavelengthGrid, CalcTransmissivity, "k-", label="Current Model")
plt.xlabel("Wavelength (microns)", fontsize=20)
plt.ylabel("Transmissivity", fontsize=20)
plt.yscale('log')
plt.ylim(1.1, 1e-9)
plt.xlim(1.0, 10.0)
plt.legend(loc=2)
plt.tight_layout()
#plt.savefig("ModelComparison.png") #If you want to save as png and include it in your assignment set.
plt.show()
