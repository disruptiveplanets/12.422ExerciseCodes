from hapi import *

#Suspected molecules in Proxima cen b

#Let's download into data folder
fetch('data/CO2',2,1,1000, 10000) #Download from 1 microns to 10 micron range. 1000 per cm = 10 microns and 10000 per cm is 1 microns
fetch('data/H2O',1,1, 1000, 10000)
fetch('data/CO',5,1, 1000, 10000)
fetch('data/NH3',11,1, 1000, 10000)
fetch('data/PH3',28,1, 1000, 10000)
