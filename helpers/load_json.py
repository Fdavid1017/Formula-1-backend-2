import json


def load_json(file_location):
    f = open(file_location)
    data = json.load(f)
    return data
