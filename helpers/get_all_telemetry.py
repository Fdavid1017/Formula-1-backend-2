from pprint import pprint

import fastf1 as ff1


def get_all_lap_data(year, gp, session, fields=None, lap=None):
    race = ff1.get_session(year, gp, session)
    laps = race.load_laps(with_telemetry=True)
    telemetry=laps.get_telemetry()

    pprint(telemetry.T)

    if lap is not None:
        laps = laps.loc[laps['LapNumber'] == int(lap)]

    if fields is not None:
        return laps[fields]

    pprint(laps)
    return laps
