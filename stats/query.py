import requests
import json
from tokens import key
from players import uuid


def get_bedwars_stats(username):
    user = uuid(username)
    URL = f"https://api.hypixel.net/player?key={key}&uuid={user}"
    DATA = requests.get(URL).json()
    bedwars_stats = DATA["player"]["stats"]["Bedwars"]
    print(bedwars_stats)
    return(bedwars_stats)