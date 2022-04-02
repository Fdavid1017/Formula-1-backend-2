import fastf1 as ff1
from fastf1.core import Laps


def get_laps_in_session(gp, session, year):
    session = ff1.get_session(year, gp, session)
    laps = session.load_laps()
    largest_lap_number = Laps(laps).sort_values(by='LapNumber', ascending=False).reset_index(drop=True)

    return largest_lap_number[['LapNumber']].iloc[0]['LapNumber']
