#! /usr/bin/env python3

import requests

#Test the third case of GET a download of specific robot

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "api/robot/puma.json/download")
print(response.json())