from fastf1.core import NoLapDataError
from flask import jsonify
from flask_restful import Resource

from helpers.ergast_api_helper import get_race_result
from helpers.handle_endpoint_exception import handle_endpoint_exception


class RaceResult(Resource):
    def get(self, round, year):
        try:
            return jsonify(get_race_result(round, year))
        except NoLapDataError as e:
            return handle_endpoint_exception(str(e), 404)
        except Exception as e:
            return handle_endpoint_exception(str(e), 500)
