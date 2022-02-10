import json

from flask import Response


def handle_endpoint_exception(message,status):
    print(message)
    return Response(
        response=json.dumps({'error': message}),
        status=status, mimetype='application/json')

