import matplotlib.pyplot as plt
import pyshtools as pysh
from pyshtools import constants

from cartopy import crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from rasterio.transform import from_bounds

import xarray as xr

if __name__ == "__main__":

    """
    Importing the spherical harmonics coefficients for Venus' gravity field from pyshtools dataset 
    from JPL 180 degree and order spherical harmonic model of the gravitational potential of Venus 
    (Konopliv et al. 1999).
    """
    clm = pysh.datasets.Venus.MGNP180U()

    """
    Importing the spherical harmonics coefficients for Venus' topography from pyshtools dataset 
    from 719 degree and order spherical harmonic model of the shape of the planet Venus (Wieczorek 2015).
    """
    shape = pysh.datasets.Venus.VenusTopo719(lmax=719)

    """
    Defining planetary contants for Venus. 

    a = the semimajor axis
    r0 = reference radius
    o = angular velocity
    gm = standard gravitational parameter
    rho = mean density
    """
    a = constants.Venus.gravity_mean_radius.value
    r0 = 6051000.0 # m
    o = -2.992398738488947e-07 # rad /s
    gm = 324858592079000.0 #m^3/s^2
    rho = 5243. #kg/m^3 

    


