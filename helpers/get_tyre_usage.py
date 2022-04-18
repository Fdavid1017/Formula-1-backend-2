from pprint import pprint

import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd


def get_tyre_usage(gp, session, year=2021):
    # Load the session data
    race = ff1.get_session(year, gp, session)
    laps = race.load_laps(with_telemetry=True)

    driver_stints = laps[['Driver', 'Stint', 'Compound', 'LapNumber']].groupby(
        ['Driver', 'Stint', 'Compound']
    ).count().reset_index()

    driver_stints = driver_stints.rename(columns={'LapNumber': 'StintLength'})

    return driver_stints.sort_values(by=['Stint'])
