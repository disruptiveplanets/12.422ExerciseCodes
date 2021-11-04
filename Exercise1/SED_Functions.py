import pandas as pd
import numpy as np

def vega_to_ab(vega_magnitude, band):

    """
    Convert Vega magnitude to AB magnitude
    """

    # Get the index of the row corresponding to the specified band
    band_index = FilterTable["Band"] == band

    # Return the magnitude in the AB scale
    return vega_magnitude + FilterTable["mAB - mVega"][band_index]

# -----------------------------------------------------------------

def ab_to_vega(ab_magnitude, band):

    """
    Input Parameter
    -------------------
    ab_magnitude: Magnitude in ab scale
    band is the bandwidth
    ---------------------
    returns Vega
    """

    # Get the index of the row corresponding to the specified band
    band_index = FilterTable["Band"] == band
    # Return the magnitude in the Vega system
    return ab_magnitude - FilterTable["mAB - mVega"][band_index]

# -----------------------------------------------------------------


def ab_to_jansky(ab_mag):

    """
    Input Parameter
    -------------------
    ab_mag: Input ab magnitude of the star
    ---------------------
    returns flux in Jansky
    """
    return 10**(-(ab_mag+48.60)/2.5)*1e23 #old implemented

def jansky_to_ab(jansky_fluxes):

    """
    This function ...
    :param jansky_fluxes:
    :return:
    """

    return -5./2. * np.log10(jansky_fluxes / ab_mag_zero_point.to("Jy").value)



def GetWaveLength(Band):
    return float(ZeroPointTable[Band][0]), float(ZeroPointTable[Band][1])/2.0


def planck(T,L):
    '''
    Models the planck function
    '''
    c = 299792458 # m s^-1, courtesy Wikipedia
    h = 6.626e-34 # J s, courtesy Wikipedia
    boltzmann = 1.38e-23 # J K^-1, courtesy Wikipedia

    return 2.*h*(c**2.)/(L**5.)/np.expm1(h*c/(L*boltzmann*T))

def planckCGSLambda(T,L):
    '''
    Models the planck function
    '''
    c = 2.99792458e10 # cm s^-1, courtesy Wikipedia
    h = 6.626e-27 # CGS courtesy Wikipedia
    boltzmann = 1.3806e-16 # CGS, courtesy Wikipedia
    return np.pi*2.*h*(c**2.)/(L**5.)/np.expm1(h*c/(L*boltzmann*T))

def planckCGS(T,L):
    '''
    Models the planck function
    '''
    c = 2.99792458e10 # cm s^-1, courtesy Wikipedia
    h = 6.626e-27 # CGS courtesy Wikipedia
    boltzmann = 1.3806e-16 # CGS, courtesy Wikipedia
    nu = c/L
    return np.pi*2.*h*nu*nu*nu/(c*c)/np.expm1(h*nu/(boltzmann*T))

def ConvertMag2Flux(app_mags):
    '''
    Input Parameter:
    ###############################################
    use the dictionary of apparent parameters

    Return Parameters:
    ################################################
    Band ==== > U, B, V .....
    Filter Wavelength
    Filter range
    Flux
    FluxError
    FluxDensity
    FluxDensityError
    '''
    WaveLengthList = []
    WaveLengthRangeList = []

    FluxList = []
    FluxErrorList = []

    FluxDensityList = []
    FluxDensityErrorList = []

    BandList = []

    for Band, Value in app_mags.items():
        print(Band)
        AB_Mag = vega_to_ab(Value[0], Band).values[0]
        CurrentWaveLength, CurWaveLengthRange = GetWaveLength(Band)
        CurrentFluxDensity = ab_to_jansky(AB_Mag)
        AB_Mag_Up = vega_to_ab(Value[0] - Value[1], Band).values[0]

        FluxDensityUp = ab_to_jansky(AB_Mag_Up)
        FluxErrorDensity = np.abs(CurrentFluxDensity - FluxDensityUp)

        #Avoiding zeros
        if CurrentWaveLength>1e-18:
            WaveLengthList.append(CurrentWaveLength)
            WaveLengthRangeList.append(CurWaveLengthRange)
            BandList.append(Band)
            FluxDensityList.append(CurrentFluxDensity)
            FluxDensityErrorList.append(FluxErrorDensity)

            Frequency =   3e8/(CurrentWaveLength*1e-6)
            CurrentFlux = CurrentFluxDensity*1e-23*Frequency
            CurrentFluxError = FluxErrorDensity*1e-23*Frequency

            FluxList.append(CurrentFlux)
            FluxErrorList.append(CurrentFluxError)

    BandList = np.array(BandList)

    WaveLengthList = np.array(WaveLengthList)
    WaveLengthRangeList = np.array(WaveLengthRangeList)

    FluxList = np.array(FluxList)
    FluxErrorList = np.array(FluxErrorList)

    FluxDensityList = np.array(FluxDensityList)
    FluxDensityErrorList = np.array(FluxDensityErrorList)

    #Remove nan
    RemoveIndex = np.logical_or(np.isnan(FluxList), np.isnan(FluxErrorList))

    BandList = BandList[~RemoveIndex]

    WaveLengthList = WaveLengthList[~RemoveIndex]
    WaveLengthRangeList = WaveLengthRangeList[~RemoveIndex]

    FluxList = FluxList[~RemoveIndex]
    FluxErrorList = FluxErrorList[~RemoveIndex]

    FluxDensityList = FluxDensityList[~RemoveIndex]
    FluxDensityErrorList = FluxDensityErrorList[~RemoveIndex]

    #Arrange by increasing wavelength
    ArrangeIndex = np.argsort(WaveLengthList)

    BandList = BandList[ArrangeIndex]

    WaveLengthList = WaveLengthList[ArrangeIndex]
    WaveLengthRangeList = WaveLengthRangeList[ArrangeIndex]

    FluxList = FluxList[ArrangeIndex]
    FluxErrorList = FluxErrorList[ArrangeIndex]

    FluxDensityList = FluxDensityList[ArrangeIndex]
    FluxDensityErrorList = FluxDensityErrorList[ArrangeIndex]

    print("The final length of the bandlist is::", len(BandList))
    return BandList, WaveLengthList, WaveLengthRangeList, FluxList, \
    FluxErrorList, FluxDensityList, FluxDensityErrorList


#Read table from the local files
FilterTable = pd.read_csv("FilterData.dat",skiprows=2)
ZeroPointTable = pd.read_csv("ZeroPointFlux.dat",skiprows=2)
