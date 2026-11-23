import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("LASTFM_API_KEY")

r = requests.get("https://ws.audioscrobbler.com/2.0/", params={
    "method": "user.getrecenttracks",
    "user": "rj",
    "api_key": key,
    "format": "json",
    "limit": 5,
})
print(r.status_code)
print(r.json())
