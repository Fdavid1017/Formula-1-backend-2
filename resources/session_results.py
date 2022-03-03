import json
from pprint import pprint

from flask_restful import Resource

from helpers.get_ff1_session_results import get_session_results
from helpers.handle_endpoint_exception import handle_endpoint_exception


class SessionResults(Resource):
    def get(self, gp, session, year):
        try:
            return json.loads(get_session_results(gp, session, year).to_json())
        except Exception as e:
            return handle_endpoint_exception(str(e), 500)
