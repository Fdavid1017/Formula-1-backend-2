import fastf1
import pandas as pd
from fastf1.core import Laps


def get_session_results(gp, session, year=2021):
    session = fastf1.get_session(year, gp, session)
    laps = session.load_laps()

    ##############################################################################
    # First, we need to get an array of all drivers.

    drivers = pd.unique(laps['Driver'])

    ##############################################################################
    # After that we'll get each drivers fastest lap, create a new laps object
    # from these laps, sort them by lap time and have pandas reindex them to
    # number them nicely by starting position.

    list_fastest_laps = list()
    for drv in drivers:
        if type(drv) is str:
            try:
                drvs_fastest_lap = laps.pick_driver(drv).pick_fastest()
                list_fastest_laps.append(drvs_fastest_lap)
            except Exception:
                list_fastest_laps.append(laps.pick_driver(drv).iloc[0])

    fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)

    ##############################################################################
    # The plot is nicer to look at and more easily understandable if we just plot
    # the time differences. Therefore we subtract the fastest lap time from all
    # other lap times.

    pole_lap = fastest_laps.pick_fastest()
    fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']

    driver_full_names = []
    driver_ids = []
    colors = []
    for index, row in fastest_laps.iterrows():
        driver = session.get_driver(row['Driver'])
        driver_full_names.append(f'{driver.name} {driver.familyname}')
        driver_ids.append(driver.info['Driver']['driverId'])
        colors.append(fastf1.plotting.team_color(row['Team']))

    fastest_laps['DriverFullName'] = driver_full_names
    fastest_laps['DriverId'] = driver_ids
    fastest_laps['Color'] = colors

    return fastest_laps[[
        "Time",
        "DriverNumber",
        "LapTime",
        "LapNumber",
        "Stint",
        "Sector1Time",
        "Sector2Time",
        "Sector3Time",
        "Sector1SessionTime",
        "Sector2SessionTime",
        "Sector3SessionTime",
        "SpeedI1",
        "SpeedI2",
        "SpeedFL",
        "SpeedST",
        "Compound",
        "TyreLife",
        "FreshTyre",
        "LapStartTime",
        "Team",
        "Driver",
        "TrackStatus",
        "LapTimeDelta",
        "DriverFullName",
        "DriverId",
        "Color"
    ]]
