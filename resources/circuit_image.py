from flask import send_file
from flask_restful import Resource

from helpers.handle_endpoint_exception import handle_endpoint_exception


class CircuitImage(Resource):
    def get(self, image_name):
        try:
            return send_file(f'static/circuits_images/{image_name}', mimetype='image/gif')
        except FileNotFoundError:
            return handle_endpoint_exception('Image not found!', 404)
