#! /usr/bin/env python3

import requests

#Test the DELETE /api/robot/filename

BASE = "http://127.0.0.1:5000/"

response = requests.delete(BASE + "api/robot/puma.json")
print(response.json())