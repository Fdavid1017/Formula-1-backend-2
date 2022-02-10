import datetime

from flask import jsonify
from flask_restful import Resource

from helpers.ergast_api_helper import get_current_schedule


class UpcomingRace(Resource):
    def get(self):
        schedule = get_current_schedule()
        today = datetime.datetime.now()
        year, month, day = schedule[0]['date'].split('-')
        date = datetime.datetime(int(year), int(month), int(day))

        diff = date - today
        closest = {
            'race': schedule[0],
            'date': date,
            'diff': diff
        }
        for i in range(1, len(schedule)):
            race = schedule[i]
            year, month, day = race['date'].split('-')
            date = datetime.datetime(int(year), int(month), int(day))
            diff = date - today
            if 0 < diff.days < closest['diff'].days:
                closest = {
                    'race': race,
                    'date': date,
                    'diff': diff
                }

            if diff.days > closest['diff'].days:
                return jsonify(closest['race'])

        return
