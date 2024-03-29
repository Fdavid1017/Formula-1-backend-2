import os

import fastf1 as ff1
from fastf1 import plotting
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources import cache
from resources.all_car_data import AllCarData
from resources.all_telemetry import AllLapData
from resources.constructor_details import ConstructorDetails
from resources.constructors_standing import ConstructorsStanding
from resources.current_schedule import CurrentSchedule
from resources.driver_details import DriverDetails
from resources.drivers_standing import DriversStanding
from resources.fastest_sector_times import FastestSectorTimesWeekend
from resources.gearshifts_on_lap import GearShiftsOnLap
from resources.get_tweets import GetTweets
from resources.max_laps_in_session import MaxLapsInSession
from resources.race_results import RaceResult
from resources.scedule_infos import ScheduleInfos
from resources.session_drivers import SessionDrivers
from resources.session_results import SessionResults
from resources.speed_on_lap import SpeedOnLap
from resources.tyre_usage import TyreUsage
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
cache.init_app(app)

api.add_resource(CurrentSchedule, '/api/current-schedule', endpoint="current-schedule")
api.add_resource(ScheduleInfos, '/api/schedule/<round>', endpoint="schedule-round")
api.add_resource(UpcomingRace, '/api/upcoming-race', endpoint="upcoming-race")
api.add_resource(ConstructorsStanding, '/api/constructors-standing', endpoint="constructors-standing")
api.add_resource(ConstructorDetails, '/api/constructor/<id>', endpoint="constructor-details")
api.add_resource(DriversStanding, '/api/drivers-standing', endpoint="drivers-standing")
api.add_resource(DriverDetails, '/api/driver/<id>', endpoint="driver-details")
api.add_resource(SessionResults, '/api/session-results/<gp>/<session>/<year>', endpoint="session-results-with-year")
api.add_resource(RaceResult, '/api/race-results/<round>/<year>', endpoint="race-results-with-year")
api.add_resource(FastestSectorTimesWeekend, '/api/weekend-sector-times/<gp>/<year>',
                 endpoint="fastest-sector-times-in-weekend")
api.add_resource(GearShiftsOnLap, '/api/gear-shifts-on-lap/<lap>/<driver>/<gp>/<session>/<year>',
                 endpoint="gear-shits-on-lap")
api.add_resource(SpeedOnLap, '/api/speed-on-lap/<lap>/<driver>/<gp>/<session>/<year>',
                 endpoint="speed-on-lap")
api.add_resource(GetTweets, '/api/get-tweets', endpoint="get-tweets")
api.add_resource(AllLapData, '/api/all-lap-data/<gp>/<session>/<year>',
                 endpoint="all-lap-data")
api.add_resource(AllCarData, '/api/all-car-data/<gp>/<session>/<year>/<lap>',
                 endpoint="all-car-data", defaults={'drivers_to_search': []})
api.add_resource(AllCarData, '/api/all-car-data/<gp>/<session>/<year>/<lap>/<drivers_to_search>',
                 endpoint="all-car-data-filtered")
api.add_resource(MaxLapsInSession, '/api/max-laps-in-session/<gp>/<session>/<year>', endpoint="max-laps-in-session")
api.add_resource(SessionDrivers, '/api/session-drivers/<gp>/<session>/<year>', endpoint="session-drivers")
api.add_resource(TyreUsage, '/api/tyre-usage/<gp>/<session>/<year>', endpoint="tyre-usage")

if __name__ == "__main__":
    app.run(debug=True)
