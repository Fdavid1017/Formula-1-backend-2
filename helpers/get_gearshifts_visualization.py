from io import BytesIO

import fastf1
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.collections import LineCollection


def get_gearshifts_visualization(gp, session, year, lap, driver):
    session = fastf1.get_session(year, gp, session)
    laps = session.load_laps(with_telemetry=True)
    driver_laps = laps.pick_driver(driver)

    lap = driver_laps.loc[driver_laps['LapNumber'] == int(lap)]
    tel = lap.get_telemetry()

    ##############################################################################
    # Prepare the data for plotting by converting it to the appropriate numpy
    # data types

    x = np.array(tel['X'].values)
    y = np.array(tel['Y'].values)

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    gear = tel['nGear'].to_numpy().astype(float)

    ##############################################################################
    # Create a line collection. Set a segmented colormap and normalize the plot
    # to full integer values of the colormap

    cmap = cm.get_cmap('Paired')
    lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N + 1), cmap=cmap)
    lc_comp.set_array(gear)
    lc_comp.set_linewidth(4)
    # sphinx_gallery_defer_figures

    ##############################################################################
    # Create the plot

    plt.figure(facecolor='white')
    plt.gca().add_collection(lc_comp)
    plt.axis('equal')
    plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

    ##############################################################################
    # Add a colorbar to the plot. Shift the colorbar ticks by +0.5 so that they
    # are centered for each color segment.

    cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
    cbar.set_ticks(np.arange(1.5, 9.5))
    cbar.set_ticklabels(np.arange(1, 9), color="black")
    cbar.set_label('Gear', color="black")

    figfile = BytesIO()
    plt.savefig(figfile, format='png', transparent=True)
    figfile.seek(0)
    return figfile
