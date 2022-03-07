from flask import jsonify
from flask_restful import Resource

from helpers.get_laps_in_session import get_laps_in_session


class MaxLapsInSession(Resource):
    def get(self, gp, session, year):
        return jsonify({
            'largestLapNumber': int(get_laps_in_session(gp, session, year))
        })
