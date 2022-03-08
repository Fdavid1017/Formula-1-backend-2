import json

import fastf1
import fastf1 as ff1
import pandas as pd


def get_all_car_data(year, gp, session, lap, drivers_to_search=[]):
    session = ff1.get_session(year, gp, session)
    laps = session.load_laps(with_telemetry=True)

    drivers = pd.unique(laps['Driver'])
    drivers_list = []
    driver_laps_list = list()

    if drivers_to_search == []:
        drivers_list = drivers
    else:
        for drv in drivers_to_search:
            if drv in drivers:
                drivers_list.append(drv)

    for drv in drivers_list:
        if type(drv) is str:
            try:
                driver_laps = laps.pick_driver(drv)
                driver_lap = driver_laps.loc[driver_laps['LapNumber'] == int(lap)]

                driver = session.get_driver(drv)
                full_name = f'{driver.name} {driver.familyname}'
                driver_id = driver.info['Driver']['driverId']
                color = fastf1.plotting.team_color(driver.team)
                team = driver.team
                telemetry = driver_lap.get_car_data().add_distance()

                telemetry = telemetry[[
                    'SessionTime',
                    'RPM',
                    'Speed',
                    'nGear',
                    'Throttle',
                    'Brake',
                    'DRS',
                    'Distance',
                ]]

                driver_laps_list.append({
                    'fullName': full_name,
                    'driverId': driver_id,
                    'color': color,
                    'team': team,
                    'carData': json.loads(telemetry.to_json()),
                })
            except Exception as e:
                print(e)

    return driver_laps_list
