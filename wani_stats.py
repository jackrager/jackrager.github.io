import requests as re
from datetime import datetime as dt

api_key = '89c801e2-6144-4bb1-a0bb-a5d8f8a8a35e'
get_endpoint = 'https://api.wanikani.com/v2/level_progressions'
response = re.get(get_endpoint, headers = {"Authorization": "Bearer " + api_key})

for each in response.json()["data"]:
	print('Level - ' + str(each["data"]["level"]))