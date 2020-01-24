from flask import Flask
from flask_restful import Resource, Api
from random import randint

values = [ 'FOO', 'BAR', 'BAZ' ]

app = Flask(__name__)
api = Api(app)

class RandomValue(Resource):
    def get(self):
        return values[randint(0, len(values) - 1)]

api.add_resource(RandomValue, '/value')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
