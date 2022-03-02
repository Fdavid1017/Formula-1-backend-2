import json

import fastf1 as ff1


def get_fastest_sector_times(gp, session, year):
    race = ff1.get_session(year, gp, session)
    laps = race.load_laps(with_telemetry=True)

    fastest_sector1 = laps[['Driver', 'Sector1Time']].groupby(['Driver']).max().sort_values('Sector1Time',
                                                                                            ascending=True)
    fastest_sector2 = laps[['Driver', 'Sector2Time']].groupby(['Driver']).max().sort_values('Sector2Time',
                                                                                            ascending=True)
    fastest_sector3 = laps[['Driver', 'Sector3Time']].groupby(['Driver']).max().sort_values('Sector3Time',
                                                                                            ascending=True)

    fastest_sector1_json = json.loads(fastest_sector1.head(1).to_json())
    fastest_sector2_json = json.loads(fastest_sector2.head(1).to_json())
    fastest_sector3_json = json.loads(fastest_sector3.head(1).to_json())

    key1 = list(fastest_sector1_json['Sector1Time'].keys())[0]
    key2 = list(fastest_sector2_json['Sector2Time'].keys())[0]
    key3 = list(fastest_sector3_json['Sector3Time'].keys())[0]

    return {
        "sector1": {
            'driver': key1,
            'time': fastest_sector1_json['Sector1Time'][key1] / 1000,
            'sessionName': session
        },
        "sector2": {
            'driver': key2,
            'time': fastest_sector2_json['Sector2Time'][key2] / 1000,
            'sessionName': session
        },
        "sector3": {
            'driver': key3,
            'time': fastest_sector3_json['Sector3Time'][key3] / 1000,
            'sessionName': session
        }

    }


def get_fastest_sector_times_weekend(gp, year):
    fp1_sectors = get_fastest_sector_times(gp, 'FP1', year)
    fp2_sectors = get_fastest_sector_times(gp, 'FP2', year)
    fp3_sectors = get_fastest_sector_times(gp, 'FP3', year)
    q_sectors = get_fastest_sector_times(gp, 'Q', year)
    r_sectors = get_fastest_sector_times(gp, 'R', year)

    sessions = [fp2_sectors, fp3_sectors, q_sectors, r_sectors]
    overall_fastest_sectors = fp1_sectors

    for session in sessions:
        if overall_fastest_sectors['sector1']['time'] > session['sector1']['time']:
            overall_fastest_sectors['sector1'] = session['sector1']

        if overall_fastest_sectors['sector2']['time'] > session['sector2']['time']:
            overall_fastest_sectors['sector2'] = session['sector2']

        if overall_fastest_sectors['sector3']['time'] > session['sector3']['time']:
            overall_fastest_sectors['sector3'] = session['sector3']

    return overall_fastest_sectors
