from flask import jsonify
from flask_restful import Resource

from helpers.get_fastest_sector_times import get_fastest_sector_times_weekend
from . import cache


class FastestSectorTimesWeekend(Resource):
    @cache.cached(timeout=None)
    def get(self, gp, year):
        return jsonify(get_fastest_sector_times_weekend(gp, year))
