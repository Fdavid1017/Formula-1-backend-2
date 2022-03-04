import json

import fastf1
import fastf1 as ff1
import pandas as pd


def get_all_lap_data(year, gp, session, fields=None, lap=None):
    session = ff1.get_session(year, gp, session)
    laps = session.load_laps(with_telemetry=True)

    drivers = pd.unique(laps['Driver'])
    driver_laps_list = list()

    for drv in drivers:
        if type(drv) is str:
            try:
                driver_laps = laps.pick_driver(drv)
                driver_full_names = []
                driver_ids = []
                colors = []
                for index, row in driver_laps.iterrows():
                    driver = session.get_driver(row['Driver'])
                    driver_full_names.append(f'{driver.name} {driver.familyname}')
                    driver_ids.append(driver.info['Driver']['driverId'])
                    colors.append(fastf1.plotting.team_color(row['Team']))

                driver_laps['DriverFullName'] = driver_full_names
                driver_laps['DriverId'] = driver_ids
                driver_laps['Color'] = colors

                # driver_laps = driver_laps[
                #     ['LapTime', 'DriverNumber', 'Stint', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'SpeedI1',
                #      'SpeedI2',
                #      'SpeedFL', 'SpeedST', 'TyreLife', 'LapStartTime', 'Driver']
                # ]
                driver_laps = driver_laps[[
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
                    "DriverFullName",
                    "DriverId",
                    "Color"
                ]]
                driver_laps_list.append(
                    json.loads(driver_laps.to_json())
                )
            except Exception as e:
                print(e)

    return driver_laps_list
