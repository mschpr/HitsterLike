import json
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.spotify.com/v1/tracks/"
headers = {
    'Authorization': 'Bearer ' + API_KEY
}

with open("./data/gameset_database_raw.json", "r") as file:
    gamesetSpotify = json.load(file)

gamesetLength = len(gamesetSpotify['gameset_data']['cards'])

for index, card in enumerate(gamesetSpotify['gameset_data']['cards'], start=1):
    response = requests.get(url + card['Spotify'], headers= headers)
    trackObject = response.json()
    card['ISRC'] = trackObject['external_ids']['isrc']
    time.sleep(0.1)
    print(f"{index} / {gamesetLength}")
    
with open("./data/gameset_database_isrc.json", "w") as file:
    json.dump(gamesetSpotify, file)
