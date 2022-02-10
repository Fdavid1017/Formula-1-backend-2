from flask import jsonify
from flask_restful import Resource, reqparse

from exceptions.api_request_exception import ApiRequestException
from exceptions.not_found_exception import NotFoundException
from helpers.ergast_api_helper import get_current_schedule
from helpers.handle_endpoint_exception import handle_endpoint_exception


class CurrentSchedule(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('expand-circuit', type=bool, default=False)
        self.reqparse.add_argument('expand-circuit-image', type=bool, default=False)
        self.reqparse.add_argument('expand-circuit-map', type=bool, default=False)

    def get(self):
        args = self.reqparse.parse_args()

        try:
            expand = {
                'infos': args['expand-circuit'],
                'image': args['expand-circuit-image'],
                'map': args['expand-circuit-map']
            }
            return jsonify(get_current_schedule(expand))
        except ApiRequestException as e:
            return handle_endpoint_exception(str(e), 500)
        except NotFoundException as e:
            return handle_endpoint_exception(str(e), 500)
        except KeyError as e:
            return handle_endpoint_exception(str(e), 500)
