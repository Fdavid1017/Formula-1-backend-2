from flask import jsonify
from flask_restful import Resource

from exceptions.api_request_exception import ApiRequestException
from helpers.ergast_api_helper import get_current_drivers_standing
from helpers.handle_endpoint_exception import handle_endpoint_exception


class DriversStanding(Resource):
    def get(self):
        try:
            return jsonify(get_current_drivers_standing())
        except ApiRequestException as e:
            return handle_endpoint_exception(str(e), 500)
