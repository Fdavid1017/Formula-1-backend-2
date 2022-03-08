from flask import Response
from flask_restful import Resource
from helpers.get_gearshifts_visualization import get_gearshifts_visualization
from helpers.handle_endpoint_exception import handle_endpoint_exception


class GearShiftsOnLap(Resource):
    def get(self, lap, gp, session, year, driver):
        try:
            image_data = get_gearshifts_visualization(gp, session, year, lap, driver)
            return Response(image_data, mimetype='image/png')
        except Exception as e:
            return handle_endpoint_exception(str(e), 500)
