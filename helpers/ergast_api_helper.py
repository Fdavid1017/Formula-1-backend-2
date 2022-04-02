from pprint import pprint

import requests

from exceptions.api_request_exception import ApiRequestException
from exceptions.not_found_exception import NotFoundException
from helpers.circuits.circuits import get_circuit
from helpers.team_color_codes import team_color_codes
from helpers.team_full_names import team_full_names

season = 'current'


def get_current_schedule(expand=None):
    if expand is None:
        expand = {}
    response = requests.get(f'https://ergast.com/api/f1/{season}.json')

    if response.status_code != 200:
        raise ApiRequestException(f'Api responded with status code {response.status_code}')

    result = response.json()['MRData']['RaceTable']['Races']

    if 'infos' in expand and expand['infos']:
        for circuit in result:
            circuit_details = get_circuit(circuit['Circuit']['circuitId'])

            circuit['Circuit']['details'] = circuit_details

    return result


def get_schedule_by_round(round):
    schedules = get_current_schedule({
        'infos': True,
        'map': True
    })
    pprint(schedules)
    for schedule in schedules:
        pprint(schedule)
        if int(schedule['round']) == int(round):
            return schedule

    raise NotFoundException('No scheduled weekend found with the round of ' + round)


def get_current_constructors_standing():
    response = requests.get(f'https://ergast.com/api/f1/{season}/constructorStandings.json')
    if response.status_code != 200:
        raise ApiRequestException(f'Api responded with status code {response.status_code}')

    data = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    for d in data:
        id = d['Constructor']['constructorId']
        d['color'] = team_color_codes[id]
        d['nameExtended'] = team_full_names[id]

    return data


def get_current_drivers_standing():
    response = requests.get(f'https://ergast.com/api/f1/{season}/driverStandings.json')
    if response.status_code != 200:
        raise ApiRequestException(f'Api responded with status code {response.status_code}')

    drivers = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    for d in drivers:
        d['Constructors'] = d['Constructors'][0]
        d['Constructors'] = get_constructor_details(d['Constructors']['constructorId'], True)

    return drivers


def get_constructor_details(id, ignore_drivers=False):
    constructors = get_current_constructors_standing()

    constructor = None

    for c in constructors:
        if c['Constructor']['constructorId'] == id:
            constructor = c
            break

    if constructor is None:
        raise NotFoundException('Constructor not found with the id of ' + id)

    constructor['drivers'] = []

    if not ignore_drivers:
        drivers = get_current_drivers_standing()
        for driver in drivers:
            if constructor['Constructor']['constructorId'] == driver['Constructors']['Constructor']['constructorId']:
                constructor['drivers'].append({
                    'id': driver['Driver']['driverId'],
                    'code': driver['Driver']['code']
                })

    return constructor


def get_driver_details(id):
    drivers = get_current_drivers_standing()
    driver = None

    for d in drivers:
        if d['Driver']['driverId'] == id:
            driver = d
            break

    if driver is None:
        raise NotFoundException('Driver not found with the id of ' + id)

    return driver


def get_race_result(round, year):
    response = requests.get(f'https://ergast.com/api/f1/{year}/{round}/results.json')

    if response.status_code != 200:
        raise ApiRequestException(f'Api responded with status code {response.status_code}')

    result = response.json()['MRData']['RaceTable']['Races'][0]['Results']

    for i in range(len(result)):
        del (result[i]['Constructor'])
        result[i]['Driver'] = get_driver_details(result[i]['Driver']['driverId'])

    return result
