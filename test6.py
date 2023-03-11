#! /usr/bin/env python3

import requests

#Test the second case of POST a new robot, changes the name to adidas

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "api/robot", json={"filepath": "robots/kawada.json"})
print(response.json())

response = requests.get(BASE + "api/robot")
print(response.json())