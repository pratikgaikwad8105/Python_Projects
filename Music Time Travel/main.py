import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "4b74bfa16f8041c6838212d221f7950c"
CLIENT_SECRET = "be9f4f9646ee4c8c94c72237dcbac788"

date = input("Which Year you  want to travel to ? Write a date in YYYY-MM-DD format :\n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

song_names_spans = soup.select("li ul li h3")

song_list = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://www.billboard.com/charts/hot-100/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Billboard Top 100",
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)