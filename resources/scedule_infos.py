from flask import jsonify
from flask_restful import Resource

from exceptions.api_request_exception import ApiRequestException
from exceptions.not_found_exception import NotFoundException
from helpers.ergast_api_helper import get_schedule_by_round
from helpers.handle_endpoint_exception import handle_endpoint_exception


class ScheduleInfos(Resource):
    def get(self, round):
        try:
            return jsonify(get_schedule_by_round(round))
        except ApiRequestException as e:
            return handle_endpoint_exception(str(e), 500)
        except NotFoundException as e:
            return handle_endpoint_exception(str(e), 500)
        except KeyError as e:
            return handle_endpoint_exception(str(e), 500)
