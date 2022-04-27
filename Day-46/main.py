from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

APP_CLIENT_ID = os.environ.get('APP_CLIENT_ID')
APP_CLIENT_SECRET = os.environ.get('APP_CLIENT_SECRET')
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"


# Scraping Billboard 100
date = input("which year do you want to travel to? Type the date in this formate 'YYYY-MM-DD: ")
url = f"{BILLBOARD_URL}{date}"
responses = requests.get(url)
web_content = responses.text

soup = BeautifulSoup(web_content, "html.parser")
songs = soup.select(selector="li ul li h3")
song_names = [song.getText().strip("\n \t") for song in songs]


#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=APP_CLIENT_ID,
        client_secret=APP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="Day-46/token.txt"
    )
    )
user_id = sp.current_user()["id"]
print(user_id)


#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


