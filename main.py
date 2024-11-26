from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Set up the authentication flow
scope = "user-read-private user-read-email"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="http://localhost",
                                               scope='user-top-read'))


user = sp.current_user()

top_tracks = sp.current_user_top_tracks(limit=50, time_range='medium_term')

for track in top_tracks['items']:
    print(track['name'], 'by', track['artists'][0]['name'])
    
    
