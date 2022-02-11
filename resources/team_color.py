from flask import jsonify
from flask_restful import Resource

from helpers.team_color_codes import team_color_codes


class TeamColor(Resource):
    def get(self, team_id):
        return jsonify(team_color_codes[team_id])
