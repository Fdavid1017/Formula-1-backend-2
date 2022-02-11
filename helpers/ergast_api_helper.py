import requests

from exceptions.api_request_exception import ApiRequestException
from helpers.circuits.circuits import get_circuit
from helpers.load_json import load_json
from helpers.team_color_codes import team_color_codes

season = 'current'


def get_current_schedule(expand={}):
    response = requests.get(f'https://ergast.com/api/f1/{season}.json')

    if response.status_code != 200:
        raise ApiRequestException(f'Api responded with status code {response.status_code}')

    result = response.json()['MRData']['RaceTable']['Races']

    if 'infos' in expand and expand['infos']:
        for circuit in result:
            circuit_details = get_circuit(circuit['Circuit']['circuitId'])

            circuit['Circuit']['details'] = circuit_details
            if 'map' in expand and expand['map']:
                circuit['Circuit']['details']['map'] = load_json(
                    f'helpers/circuits/gjson_data/{circuit_details["gjson_map"]}')

    return result


def get_current_constructors_standing():
    response = requests.get(f'https://ergast.com/api/f1/{season}/constructorStandings.json')
    if response.status_code != 200:
        raise ApiRequestException(f'Api responded with status code {response.status_code}')

    data = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    for d in data:
        id = d['Constructor']['constructorId']
        d['color'] = team_color_codes[id]

    return data


def get_current_drivers_standing():
    response = requests.get(f'https://ergast.com/api/f1/{season}/driverStandings.json')
    if response.status_code != 200:
        raise ApiRequestException(f'Api responded with status code {response.status_code}')

    return response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
