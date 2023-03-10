#! /usr/bin/env python3

import json
from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__)
api = Api(app)


robots = [
    {
        'filename': 'testRobot1',
        'name': 'robot1',
        'filecontent' : '',
        # 'isRobot': True
    },
    {
        'filename': "testRobot2",
        'name': 'robot2',
        'filecontent' : '',
        # 'isRobot': True
    }
]

robot_put_args = reqparse.RequestParser()
robot_put_args.reqparse.add_argument('filename', type=str, location='json')
robot_put_args.reqparse.add_argument('name', type=str, location='json')

robot_attributes = {
    'filename': fields.String,
    'name': fields.String, 
    #'filecontent' : fields.String,
    # "isRobot": fields.Boolean,
}

robot_download = {
    'filecontent': fields.String,
}


def readRobotJson(filepath):
    f = open(filepath)

    filename = filepath.split('/')[1]
    data = json.load(f)
    file_content = json.dumps(data)

    name = data['bodies'][0]['name']

    robot_obj = {'filename': filename, 'name': name, 'filecontent': file_content}
    robots.append(robot_obj)


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

    def get(self, filename, download=None):
        robot = [robot for robot in robots if robot['filename'] == filename]
        if len(robot) == 0:
            abort(404, message="Cannot find this robot $filename")

        if(download == 'download'):
            return {'robot': marshal(robot[0], robot_download)}
        else:
            return {'robot': marshal(robot[0], robot_attributes)}


    def put(self, filename):
        robot = [robot for robot in robots if robot['filename'] == filename]
        if len(robot) == 0:
            abort(404, message="Cannot find this robot $filename")
        robot = robot[0]
        args = robot_put_args.parse_args()
        for key, val in args.items():

            if val is not None:
                robot[key] = val
        return {"robot": marshal(robot[0], robot_attributes)}

    def delete(self, filename):
    	for idx, robot in enumerate(robots):
    		if robot['filename'] == filename:
    			robots.pop(idx)


api.add_resource(RobotList, '/api/robot', endpoint='robots')
api.add_resource(Robot, '/api/robot/<string:filename>', '/api/robot/<string:filename>/<string:download>', endpoint='robot')



if __name__ == "__main__":
    readRobotJson('robots/puma.json')
    app.run(debug=True)