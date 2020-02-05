from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Value(Resource):
    def get(self):
        return "foo", 200

api.add_resource(Value, '/value')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
