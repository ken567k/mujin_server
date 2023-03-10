#! /usr/bin/env python3

import requests

#Test the first case of GET all properties

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "api/robot")
print(response.json())