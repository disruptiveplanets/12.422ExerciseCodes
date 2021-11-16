#Code create by Prajwal Niraula for 12.422/12.622
import hapi
import numpy as np
import matplotlib.pyplot as plt


#Create a grid of stopping wavelength

hapi.db_begin('data') #Load everything in the data website


#Let's make some absortion cross-section
nu_Voigt, coef_Voigt = hapi.absorptionCoefficient_Voigt(SourceTables='CO2', Diluent={'air':1}, \
				Environment={'p':1.0, 'T':296}, OmegaStep=0.01)

#Convert the wavenumbers to microns
WavelengthGrid = 1/nu_Voigt*1e4


#This is for plotting
plt.figure(figsize=(12,7))
plt.plot(WavelengthGrid[::-1], coef_Voigt[::-1], "k-")
plt.xlabel("Wavelength (microns)", fontsize=20)
plt.ylabel("Absortion Cross-section \n (cm-2/molecule)", fontsize=20)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig("CO2.png")
plt.show()
