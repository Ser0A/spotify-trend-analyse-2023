import requests
import pandas as pd

# Spotify API 
TOKEN_URL = "https://accounts.spotify.com/api/token"
SEARCH_URL = "https://api.spotify.com/v1/search"
TRACK_URL = "https://api.spotify.com/v1/tracks/{id}"

CLIENT_ID = "d1afc30fc0c146a691160bcbab3cceb8"
CLIENT_SECRET = "Gebruik eigen ID"

def get_token(client_id, client_secret):
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(TOKEN_URL, data=payload)
    token = response.json().get("access_token")
    return token

# album cover URL
def get_album_cover_url(track_name, artist_name, token):
    headers = {
        'Authorization': f"Bearer {token}",
    }
    params = {
        'q': f"track:{track_name} artist:{artist_name}",
        'type': 'track',
        'limit': 1
    }
    response = requests.get(SEARCH_URL, headers=headers, params=params)
    tracks = response.json().get("tracks", {}).get("items", [])
    
    if tracks:
        track_id = tracks[0].get("id")
        track_data = requests.get(TRACK_URL.format(id=track_id), headers=headers).json()
        album_cover_url = track_data["album"]["images"][0]["url"]
        return album_cover_url
    return None

df = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

df['album_cover_url'] = None

token = get_token(CLIENT_ID, CLIENT_SECRET)

for index, row in df.iterrows():
    track_name = row['track_name']
    artist_name = row['artist(s)_name']
    
    url = get_album_cover_url(track_name, artist_name, token)
    
    df.at[index, 'album_cover_url'] = url

df.to_csv('spotify-2023-with-urls.csv', index=False)
