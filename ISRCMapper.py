import json
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY_Tidal")
url = "https://openapi.tidal.com/v2/tracks"
headers = {
    'Authorization': 'Bearer ' + API_KEY
}

with open("./data/gameset_database_isrc.json", "r") as file:
    gamesetISRC = json.load(file)

gamesetLength = len(gamesetISRC['gameset_data']['cards'])

for index, card in enumerate(gamesetISRC['gameset_data']['cards'], start=1):
    params = {
        'filter[isrc]': {card['ISRC']}
    }
    response = requests.get(url=url, headers= headers, params=params)
    trackObject = response.json()
    if len(trackObject['data'] == 0):
        print(f"{card['Spotify']} could not be matched via ISRC")
    else:
        card['Tidal'] = trackObject['data'][0]['id']
    time.sleep(0.1)
    print(f"{index} / {gamesetLength}")

with open("./data/gameset_database_tidal.json", "w") as file:
    json.dump(gamesetISRC, file)
