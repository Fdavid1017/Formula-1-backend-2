from flask import jsonify
from flask_restful import Resource

from helpers.get_distance_between_drivers import get_distance_between_drivers


class DistanceBetweenDrivers(Resource):
    def get(self, gp, session,year, driver1, driver2):
        try:
            return jsonify(get_distance_between_drivers(year, gp, session, driver1, driver2).to_json())
        except Exception as e:
            return jsonify(e)
