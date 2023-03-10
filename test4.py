#! /usr/bin/env python3

import requests

#Test the second case of GET a specific robot, changes the name to adidas

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "api/robot/puma.json", {"filename": "puma.json", "name": "adidas"})
print(response.json())