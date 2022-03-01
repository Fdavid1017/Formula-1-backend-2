import os

import fastf1 as ff1
from fastf1 import plotting
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.all_team_color import AllTeamColor
from resources.all_telemetry import AllLapData
from resources.car_image import CarImage
from resources.circuit_image import CircuitImage
from resources.circuit_infos import CircuitInfos
from resources.constructor_details import ConstructorDetails
from resources.constructors_standing import ConstructorsStanding
from resources.current_schedule import CurrentSchedule
from resources.distance_between_drivers import DistanceBetweenDrivers
from resources.driver_details import DriverDetails
from resources.driver_image import DriverImage
from resources.drivers_standing import DriversStanding
from resources.gearshifts_on_lap import GearShiftsOnLap
from resources.get_tweets import GetTweets
from resources.scedule_infos import ScheduleInfos
from resources.session_results import SessionResults
from resources.speed_on_lap import SpeedOnLap
from resources.team_color import TeamColor
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
api.add_resource(ScheduleInfos, '/api/schedule/<round>', endpoint="schedule-round")
api.add_resource(CircuitImage, '/api/circuit-image/<image_name>', endpoint="circuit-image")
api.add_resource(DriverImage, '/api/driver-image/<image_name>', endpoint="driver-image")
api.add_resource(CarImage, '/api/car-image/<image_name>', endpoint="car-image")
api.add_resource(UpcomingRace, '/api/upcoming-race', endpoint="upcoming-race")
api.add_resource(ConstructorsStanding, '/api/constructors-standing', endpoint="constructors-standing")
api.add_resource(ConstructorDetails, '/api/constructor/<id>', endpoint="constructor-details")
api.add_resource(DriversStanding, '/api/drivers-standing', endpoint="drivers-standing")
api.add_resource(DriverDetails, '/api/driver/<id>', endpoint="driver-details")
api.add_resource(SessionResults, '/api/session-results/<gp>/<session>/<year>', endpoint="session-results-with-year")
api.add_resource(GearShiftsOnLap, '/api/gear-shifts-on-lap/<lap>/<driver>/<gp>/<session>/<year>',
                 endpoint="gear-shits-on-lap")
api.add_resource(SpeedOnLap, '/api/speed-on-lap/<lap>/<driver>/<gp>/<session>/<year>',
                 endpoint="speed-on-lap")
api.add_resource(GetTweets, '/api/get-tweets',
                 endpoint="get-tweets")
api.add_resource(TeamColor, '/api/team-colors/<team_id>', endpoint="team-color")
api.add_resource(AllTeamColor, '/api/team-colors', endpoint="all-team-color")
api.add_resource(CircuitInfos, '/api/circuit/<circuit_id>', endpoint="circuit-infos")
api.add_resource(DistanceBetweenDrivers, '/api/distance-between-drivers/<gp>/<session>/<year>/<driver1>/<driver2>',
                 endpoint="distance-between-drivers")
api.add_resource(AllLapData, '/api/all-lap-data/<gp>/<session>/<year>',
                 endpoint="all-lap-data")

if __name__ == "__main__":
    app.run(debug=True)
