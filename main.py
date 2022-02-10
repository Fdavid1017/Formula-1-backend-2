import os

import fastf1 as ff1
from fastf1 import plotting
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.car_image import CarImage
from resources.circuit_image import CircuitImage
from resources.constructors_standing import ConstructorsStanding
from resources.current_schedule import CurrentSchedule
from resources.driver_image import DriverImage
from resources.drivers_standing import DriversStanding
from resources.gearshifts_on_lap import GearShiftsOnLap
from resources.session_results import SessionResults
from resources.upcoming_race import UpcomingRace

plotting.setup_mpl()

fast_f1_cache_folder = 'fast_f1_cache'

# Check whether the specified path exists or not
if not os.path.exists(fast_f1_cache_folder):
    os.makedirs(fast_f1_cache_folder)

ff1.Cache.enable_cache(fast_f1_cache_folder)

app = Flask(__name__, static_url_path='/static')
app.debug = True
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

api.add_resource(CurrentSchedule, '/api/current-schedule', endpoint="current-schedule")
api.add_resource(CircuitImage, '/api/circuit-image/<image_name>', endpoint="circuit-image")
api.add_resource(DriverImage, '/api/driver-image/<image_name>', endpoint="driver-image")
api.add_resource(CarImage, '/api/car-image/<image_name>', endpoint="car-image")
api.add_resource(UpcomingRace, '/api/upcoming-race', endpoint="upcoming-race")
api.add_resource(ConstructorsStanding, '/api/constructors-standing', endpoint="constructors-standing")
api.add_resource(DriversStanding, '/api/drivers-standing', endpoint="drivers-standing")
api.add_resource(SessionResults, '/api/session-results/<gp>/<session>', defaults={'year': '2021'},
                 endpoint="session-results-without-year")
api.add_resource(SessionResults, '/api/session-results/<gp>/<session>/<year>', endpoint="session-results-with-year")
api.add_resource(GearShiftsOnLap, '/api/gear-shifts-in-lap/<lap>/<driver>/<gp>/<session>/<year>',
                 endpoint="gear-shits-in-lap-with-year")
api.add_resource(GearShiftsOnLap, '/api/gear-shifts-in-lap/<lap>/<driver>/<gp>/<session>', defaults={'year': '2021'},
                 endpoint="gear-shits-in-lap-without-year")

if __name__ == "__main__":
    app.run(debug=True)
