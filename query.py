from lightkurve import search_targetpixelfile
import numpy as np
from astroquery.mast import Catalogs
from astropy.coordinates import SkyCoord
import astropy.units as u

def get_objects_in_radius(radius=0.1):
    ra = np.random.uniform(0, 360)
    dec = np.random.uniform(-90, 90)
    coordinates = SkyCoord(ra, dec, unit=(u.deg, u.deg))
    result_table = Catalogs.query_region(coordinates, radius=radius, catalog="TIC")
    if len(result_table) == 0:
        return []
    object_ids = result_table['ID'].tolist()
    return object_ids

def plot_pixel_file(pixelfile, frame=1):
    pixelfile.plot(frame)

def plot_light_curve(lc):
    lc.scatter(s=0.2)

def plot_periodogram(fft):
    fft.plot()

def plot_folded(lc, period):
    folded = lc.fold(period=period)
    folded.scatter(s=0.2)

def search(name):
    pixelfiles = search_targetpixelfile(name)
    return pixelfiles

def download(name, id=0):
    pixelfiles = search_targetpixelfile(name)
    return pixelfiles[id].download(quality_bitmask='hardest')

def light_curve(pixelfile, flatten=False):
    lc = pixelfile.to_lightcurve(aperture_mask='all')
    if flatten:
        lc = lc.flatten()
    return lc

def fft_max_response(lc):
    periodogram = lc.to_periodogram(method='bls')
    return periodogram.period_at_max_power



