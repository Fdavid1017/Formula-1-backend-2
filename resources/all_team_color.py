from flask import jsonify
from flask_restful import Resource

from helpers.team_color_codes import team_color_codes


class AllTeamColor(Resource):
    def get(self):
        return jsonify(team_color_codes)
