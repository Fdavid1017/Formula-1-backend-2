from flask_restful import Resource

from helpers.circuits.circuits import get_circuit
from helpers.load_json import load_json


class CircuitInfos(Resource):
    def get(self, circuit_id):
        circuit = get_circuit(circuit_id)
        circuit['map'] = load_json(f'helpers/circuits/gjson_data/{circuit["gjson_map"]}')
        return circuit
