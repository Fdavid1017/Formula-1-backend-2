from flask import jsonify
from flask_restful import Resource

from helpers.get_speed_visualization import get_speed_visualization
from helpers.handle_endpoint_exception import handle_endpoint_exception


class SpeedOnLap(Resource):
    def get(self, lap, gp, session, year,driver):
        try:
            return jsonify(get_speed_visualization(gp, session, year, lap,driver))
        except Exception as e:
            return handle_endpoint_exception(str(e), 500)
