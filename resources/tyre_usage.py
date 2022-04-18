from flask import jsonify
from flask_restful import Resource

from helpers.get_tyre_usage import get_tyre_usage
from helpers.handle_endpoint_exception import handle_endpoint_exception
from . import cache


class TyreUsage(Resource):
    @cache.cached(timeout=None)
    def get(self, gp, session, year):
        try:
            return jsonify(get_tyre_usage(gp, session, year).to_json())
        except Exception as e:
            return handle_endpoint_exception(str(e), 500)
