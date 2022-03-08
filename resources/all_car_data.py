from flask import jsonify
from flask_restful import Resource
from helpers.get_all_car_data import get_all_car_data

from . import cache


class AllCarData(Resource):
    @cache.cached(timeout=None)
    def get(self, year, gp, session, lap, drivers_to_search):
        return jsonify(get_all_car_data(year, gp, session, lap, drivers_to_search.split(',')))
