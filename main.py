from flask import Flask
from flask_restful import Api, Resource

app = Flast(__name__)
api = Api(app)

class RobotServer(Resource):
	def get(self):
		return {"robot 1"}

api.add_resource(RobotServer, "/api")

if __name__ == "__main__":
	app.run(debug=True)