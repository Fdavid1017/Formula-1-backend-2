import fastf1
import fastf1 as ff1
import pandas as pd


def get_session_drivers(gp, session, year):
    session = ff1.get_session(year, gp, session)
    laps = session.load_laps(with_telemetry=True)
    driver_list = list()

    driver_codes = pd.unique(laps['Driver'])
    for code in driver_codes:
        if type(code) is str:
            driver = session.get_driver(code)

            full_name = f'{driver.name} {driver.familyname}'
            driver_id = driver.info['Driver']['driverId']
            number = driver.info['Driver']['permanentNumber']
            code = driver.info['Driver']['code']
            color = fastf1.plotting.team_color(driver.team)
            team = driver.team

            driver_list.append({
                'fullName': full_name,
                'driverId': driver_id,
                'permanentNumber': number,
                'color': color,
                'team': team,
                'code': code,
            })

    return driver_list
