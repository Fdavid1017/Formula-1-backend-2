from flask_restful import Resource, reqparse

from helpers.twitter_helper import get_tweets


class GetTweets(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('limit', type=int, default=10)
        self.reqparse.add_argument('token', type=str, default=None)

    def get(self):
        args = self.reqparse.parse_args()
        return get_tweets(args['limit'], args['token'])
