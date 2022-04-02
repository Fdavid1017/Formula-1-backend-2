from flask_restful import Resource

from helpers.get_all_telemetry import get_all_lap_data
from . import cache


class AllLapData(Resource):
    @cache.cached(timeout=None)
    def get(self, year, gp, session):
        return get_all_lap_data(year, gp, session)
