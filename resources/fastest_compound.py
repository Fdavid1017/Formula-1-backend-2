from flask import jsonify
from flask_restful import Resource

from helpers.get_fastest_compound import get_fastest_compound


class FastestCompound(Resource):
    def get(self, lap, gp, session, year):
        get_fastest_compound(lap, gp, session, year)
        return 'jsonify()'
