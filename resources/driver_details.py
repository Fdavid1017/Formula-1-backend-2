from flask import jsonify
from flask_restful import Resource

from exceptions.api_request_exception import ApiRequestException
from exceptions.not_found_exception import NotFoundException
from helpers.ergast_api_helper import get_driver_details
from helpers.handle_endpoint_exception import handle_endpoint_exception


class DriverDetails(Resource):
    def get(self, id):
        try:
            return jsonify(get_driver_details(id))
        except ApiRequestException as e:
            return handle_endpoint_exception(str(e), 500)
        except NotFoundException as e:
            return handle_endpoint_exception(str(e), 404)
