import io

import fastf1 as fastf1
import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection


def get_speed_visualization(gp, session, year, lap, driver):
    session = fastf1.get_session(year, gp, session)
    laps = session.load_laps(with_telemetry=True)
    driver_laps = laps.pick_driver(driver)

    lap = driver_laps.loc[driver_laps['LapNumber'] == int(lap)]
    # Get telemetry data
    x = lap.telemetry['X']  # values for x-axis
    y = lap.telemetry['Y']  # values for y-axis
    color = lap.telemetry['Speed']  # value to base color gradient on

    ##############################################################################
    # Now, we create a set of line segments so that we can color them
    # individually. This creates the points as a N x 1 x 2 array so that we can
    # stack points  together easily to get the segments. The segments array for
    # line collection needs to be (numlines) x (points per line) x 2 (for x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    ##############################################################################
    # After this, we can actually plot the data.

    # We create a plot with title and adjust some setting to make it look good.
    fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))

    # Adjust margins and turn of axis
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.12)
    ax.axis('off')

    # After this, we plot the data itself.
    # Create background track line
    ax.plot(lap.telemetry['X'], lap.telemetry['Y'], color='black', linestyle='-', linewidth=16, zorder=0)

    # Create a continuous norm to map from data points to colors
    norm = plt.Normalize(color.min(), color.max())
    colormap = mpl.cm.RdYlGn_r
    lc = LineCollection(segments, cmap=colormap, norm=norm, linestyle='-', linewidth=5)

    # Set the values used for colormapping
    lc.set_array(color)

    # Merge all line segments together
    line = ax.add_collection(lc)

    # Finally, we create a color bar as a legend.
    cbaxes = fig.add_axes([0.25, 0.05, 0.5, 0.05])
    normlegend = mpl.colors.Normalize(vmin=color.min(), vmax=color.max())
    legend = mpl.colorbar.ColorbarBase(cbaxes, norm=normlegend, cmap=colormap, orientation="horizontal")

    imgdata = io.StringIO()
    plt.savefig(imgdata, format='svg', transparent=True)
    imgdata.seek(0)  # rewind the data
    plt.show()
    return imgdata.getvalue()
