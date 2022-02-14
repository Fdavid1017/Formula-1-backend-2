import fastf1 as ff1
import numpy as np
import pandas
import pandas as pd
from fastf1 import plotting


def get_distance_between_drivers(year, gp, session, driver1, driver2):
    plotting.setup_mpl()
    pd.options.mode.chained_assignment = None

    # Load the session data
    race = ff1.get_session(year, gp, session)

    # Get the laps
    laps = race.load_laps(with_telemetry=True)

    laps_driver_1 = laps.pick_driver(driver1)
    laps_driver_2 = laps.pick_driver(driver2)

    driver_1_number = laps_driver_1['DriverNumber'].values[0]

    laps_driver_1['RaceLapNumber'] = laps_driver_1['LapNumber'] - 1
    laps_driver_2['RaceLapNumber'] = laps_driver_2['LapNumber'] - 1

    full_distance_drivers = pd.DataFrame()
    summarized_distance_drivers = pd.DataFrame()

    for lap in laps_driver_2.iterlaps():
        telemetry = lap[1].get_car_data().add_distance().add_driver_ahead()

        # Only run this loop when driver ahead is RIC, otherwise we compare wrong distance gaps
        telemetry = telemetry.loc[telemetry['DriverAhead'] == driver_1_number]

        if len(telemetry) != 0:
            # Full distance
            lap_telemetry = telemetry[['Distance', 'DistanceToDriverAhead']]
            lap_telemetry.loc[:, 'Lap'] = lap[0] + 1

            full_distance_drivers = pandas.concat([full_distance_drivers, lap_telemetry])

            # Average / median distance
            distance_mean = np.nanmean(telemetry['DistanceToDriverAhead'])
            distance_median = np.nanmedian(telemetry['DistanceToDriverAhead'])

            distance = pandas.DataFrame(data={
                'Lap': [lap[1]['LapNumber']],
                'Mean': [distance_mean],
                'Median': [distance_median]
            })
            summarized_distance_drivers = pandas.concat([summarized_distance_drivers, distance], ignore_index=True)

    return summarized_distance_drivers
