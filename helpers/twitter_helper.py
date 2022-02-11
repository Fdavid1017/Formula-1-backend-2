import os

import requests

os.environ[
    'TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAADMCQgEAAAAAJcBltuc%2FTrRwsywkf4rvVs5zRdI%3DRVXDVwOdk81p7sJXpD58sglklw95AEdYU3q3bBS5w1tIPkZ3LN'


def auth():
    return os.getenv('TOKEN')


def create_url():
    # Replace with user ID below
    user_id = 69008563
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params(limit, token):
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {
        "tweet.fields": "created_at,attachments,entities,public_metrics,text",
        "max_results": limit,
        "pagination_token": token
    }


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {auth()}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_tweets(limit, token):
    url = create_url()
    params = get_params(limit, token)
    json_response = connect_to_endpoint(url, params)

    return json_response
