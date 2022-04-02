import datetime

from flask import jsonify
from flask_restful import Resource

from helpers.ergast_api_helper import get_current_schedule


class UpcomingRace(Resource):
    def get(self):
        schedule = get_current_schedule()
        today = datetime.datetime.now()

        for i in range(len(schedule)):
            year, month, day = schedule[i]['date'].split('-')
            date = datetime.datetime(int(year), int(month), int(day))

            if (date - today).total_seconds() > 0:
                return jsonify(schedule[i])

        return schedule[len(schedule) - 1]
