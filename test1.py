#! /usr/bin/env python3

import requests

BASE = "https://127.0.0.1:5000/"

response = requests.get(BASE + "api")
print(response.json())