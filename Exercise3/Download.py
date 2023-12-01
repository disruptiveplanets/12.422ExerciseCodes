from hapi import *



#fetch('data/H2O',1,1, 1000, 10000)
#Download from 1 microns to 10 micron range. 1000 per cm = 10 microns and 10000 per cm is 1 microns
#The molecules are identified by their number in https://hitran.org/docs/iso-meta/ -- For example 1 is water. 

#Let's download into data folder. These are potential suspects for the atmospheric composition.
#fetch('data/CO',5,1,1000, 10000)
#fetch('data/O2',7,1, 1000, 10000)
#fetch('data/N2',22,1, 1000, 10000)
#fetch('data/PH3',28,1, 1000, 10000)
fetch('data/H2',45,1, 1000, 10000)
