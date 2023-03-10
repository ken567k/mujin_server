#! /usr/bin/env python3

import json
from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__)
api = Api(app)


robots = [
    # {
    #     'filename': 'testRobot1',
    #     'name': 'robot1',
    #     'isRobot': True
    # },
    # {
    #     'filename': "testRobot2",
    #     'name': 'robot2',
    #     'isRobot': True
    # }
]

robot_attributes = {
    'filename': fields.String,
    # 'name': fields.String,
    # "isRobot": fields.Boolean,
}


def readRobotJson(filename):
    f = open(filename)

    data = json.load(f)
    robots['filename'] = data

    # for i in data['bodies']:
    # 	print(i)


class RobotList(Resource):
    def get(self):
        return  {'robot': [marshal(robot, robot_attributes) for robot in robots]}

    def post(self):
        args = self.reqparse.parse_args()
        robot = {
            'filename': args['filename'],
            'name': args['name'],
            'isRobot': args['isRobot'],
        }
        robots.append(robot)
        return {'robot': marshal(robot, robot_attributes)}, 201


class Robot(Resource):
    def get(self, filename):
        robot = [robot for robot in robots if robot['filename'] == filename]
        if len(robot) == 0:
            abort(404, message="Cannot find this robot $filename")
        return {'robot': marshal(robot[0], robot_attributes)}


    def put(self, filename):
        return {"data": "Posted"}

    def delete(self, filename):
    	for idx, robot in enumerate(robots):
    		if robot['filename'] = filename:
    			robots.pop(idx)


api.add_resource(RobotList, '/api/robot', endpoint='robots')
api.add_resource(Robot, '/api/robot/<string:filename>', endpoint='robot')



if __name__ == "__main__":
    readRobotJson('robots/puma.json')
    app.run(debug=True)