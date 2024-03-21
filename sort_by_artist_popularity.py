#%%
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import pandas as pd

# Checking that your environment variables are correctly set (if you run this on your OS):
print(f'Client ID:\n{os.getenv("SPOTIPY_CLIENT_ID")}') # Get it here: https://developer.spotify.com/
print(f'Client secret:\n{os.getenv("SPOTIPY_CLIENT_SECRET")}') # Get it here: https://developer.spotify.com/
print(f'Redirect URI:\n{os.getenv("SPOTIPY_REDIRECT_URI")}') # 'http://localhost:8888/callback' (this works fine. Make sure to update it on https://developer.spotify.com/)
# YouTube tutorial for setting up the app and environment variables:
# https://www.youtube.com/watch?v=3RGm4jALukM

# Function
def sort_playlist_by_artist_popularity(playlist_url):
    print("Starting sort_playlist_by_artist_popularity")
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    print(f"Playlist ID: {playlist_id}")
    tracks_data = []

    try:
        results = sp.playlist_items(playlist_id, limit=100)
        tracks = []
        while results:
            tracks.extend(results['items'])
            if results['next']:
                results = sp.next(results)
            else:
                results = None
        print(f"Tracks fetched: {len(tracks)}")
    except Exception as e:
        print(f"Error fetching playlist items: {e}")
        return

    for i, track_item in enumerate(tracks):
        try:
            track = track_item['track']
            uri = track['uri']  
            artist_id = track['artists'][0]['id']
            artist = sp.artist(artist_id)
            artist_name = artist['name']
            artist_popularity = artist['popularity']
            genres = artist['genres']
            followers = artist['followers']['total']
            track_name = track['name']
            tracks_data.append({
                "Artist name": artist_name,
                "Artist id": artist_id,
                "Track name": track_name,
                "Artist popularity": artist_popularity,
                "Genres": genres,
                "Followers": followers,
                "uri": uri 
            })
            print(f"Processed track {i+1}/{len(tracks)} by {artist_name} - Popularity: {artist_popularity}, Followers: {followers}")
        except Exception as e:
            print(f"Error processing track {i+1}: {e}")

    # Sort tracks_data by artist popularity and followers before creating DataFrame
    sorted_tracks_data = sorted(tracks_data, key=lambda x: (x["Artist popularity"], x["Followers"]), reverse=True)
    df_tracks_sorted = pd.DataFrame(sorted_tracks_data)

    print("Tracks sorted by artist popularity and followers")

    try:
        user_id = sp.current_user()["id"]
        print(f"User ID: {user_id}")

        original_playlist = sp.playlist(playlist_id)
        original_name = original_playlist['name']
        new_playlist_name = original_name + " - sorted with Spotipy"
        new_playlist = sp.user_playlist_create(user_id, new_playlist_name, public=False)
        new_playlist_id = new_playlist["id"]
        track_uris = df_tracks_sorted["uri"].tolist() 
        print(f"Creating new playlist with ID: {new_playlist_id}")

        for i in range(0, len(track_uris), 100):
            sp.playlist_add_items(new_playlist_id, track_uris[i:i+100])
            print(f"Added tracks {i+1}-{min(i+100, len(track_uris))} to new playlist")
    except Exception as e:
        print(f"Error during playlist creation or track addition: {e}")

    return df_tracks_sorted

# %%
#sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# This will authenticate you on your web browser:
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                                               scope="playlist-modify-public playlist-modify-private"))

# Italo-Disco TEST
# playlist_url = "https://open.spotify.com/playlist/2qajcUJ7x242tTuBpEKUKx"
# Enter your playlist URL
playlist_url = input("Please enter the playlist URL: ")
df_sorted = sort_playlist_by_artist_popularity(playlist_url)
df_sorted.head(10) 
# %%
