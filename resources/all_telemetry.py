from flask import jsonify
from flask_restful import Resource

from helpers.get_all_telemetry import get_all_lap_data


class AllLapData(Resource):
    def get(self, year, gp, session):
        return jsonify(get_all_lap_data(year, gp, session).to_json())
