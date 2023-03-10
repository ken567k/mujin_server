import requests

BASE = "https://127.0.0.1:5000"

respose = requests.get(BASE + "api")
print(response.json())