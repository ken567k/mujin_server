#! /usr/bin/env python3

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class RobotServer(Resource):
	def get(self):
		return {"data": "robot 1"}

	def get(self, name):
		return {"data": name}

	def post(self):
		return {"data": "Posted"}

api.add_resource(RobotServer, "/api/robot/<string:name>")

if __name__ == "__main__":
	app.run(debug=True)