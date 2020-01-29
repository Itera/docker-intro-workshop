from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from random import randint

values = [ 'FOO', 'BAR', 'BAZ' ]

app = Flask(__name__)
api = Api(app)
CORS(app)
Swagger(app)

class RandomValue(Resource):
    def get(self):
        """
        Get a random value
        ---
        responses:
         200:
           description: A random value
           schema:
             id: value
             type: string
        """
        return values[randint(0, len(values) - 1)], 200

api.add_resource(RandomValue, '/value')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
