from flask import jsonify
from flask_restful import Resource

from exceptions.api_request_exception import ApiRequestException
from helpers.ergast_api_helper import get_constructor_details
from helpers.handle_endpoint_exception import handle_endpoint_exception


class ConstructorDetails(Resource):
    def get(self, id):
        try:
            return jsonify(get_constructor_details(id))
        except ApiRequestException as e:
            return handle_endpoint_exception(str(e), 500)
