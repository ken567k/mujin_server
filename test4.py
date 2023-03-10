#! /usr/bin/env python3

import requests

#Test the second case of GET a specific robot

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "api/robot/puma.json", {"name": "adidas"})
print(response.json())