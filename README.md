# spotipy_use_cases
This repository is a living collection of scripts and examples for different use cases of the Spotipy library, a Python library for the Spotify Web API.

# Spotipy Use Cases Repository

This repository contains examples utilizing the Spotipy library to interact with the Spotify Web API.

## Setup Requirements

- Spotify Developer account: Register your app on https://developer.spotify.com/ to get `Client ID` and `Client Secret`.
- Set `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, `SPOTIPY_REDIRECT_URI` as environment variables.
- Detailed environment setup guide: [YouTube tutorial](https://www.youtube.com/watch?v=3RGm4jALukM).

## Sort Playlist by Artist Popularity Script

The script sorts Spotify playlists by artist popularity and followers. It addresses the Spotify API's limitation on fetching data (max 100 items per request) by making paginated requests. This approach allows handling playlists with more than 100 tracks. Example: ["Seen Live" Spotify playlist with 400+ tracks](https://open.spotify.com/playlist/5ZAVOxwjVynsdh4FXypiI7?si=7fdcc8beca3b4a89)

### Functionality

- Retrieves playlist tracks and associated artist data in batches of 100.
- Sorts tracks by artist popularity and followers.
- Creates a new playlist with the sorted tracks.

### Usage

Run the script, enter the playlist URL, and a sorted version of the playlist will be created in your Spotify account. This method is effective for large playlists exceeding 100 tracks.

References within the script include the Spotify Developer portal for obtaining necessary credentials and a YouTube tutorial for setup instructions.


