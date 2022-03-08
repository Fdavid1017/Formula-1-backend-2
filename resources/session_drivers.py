from flask_restful import Resource
from helpers.get_session_drivers import get_session_drivers


class SessionDrivers(Resource):
    def get(self, gp, session, year):
        return get_session_drivers(gp, session, year)
