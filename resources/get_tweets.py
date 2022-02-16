from flask_restful import Resource, reqparse

from helpers.clamp import clamp_number
from helpers.twitter_helper import get_tweets


class GetTweets(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('limit', type=int, default=10)
        self.reqparse.add_argument('token', type=str, default=None)

    def get(self):
        args = self.reqparse.parse_args()
        limit = clamp_number(args['limit'], 5, 100)
        return get_tweets(limit, args['token'])
