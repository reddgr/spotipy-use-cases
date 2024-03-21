# spotipy_use_cases
This repository is a living collection of scripts and examples showcasing different use cases for the Spotipy library, a lightweight Python library for the Spotify Web API. 

# Spotipy Use Cases Repository

This repository is a living collection of scripts and examples showcasing different use cases for the Spotipy library, a lightweight Python library for the Spotify Web API. 

## Getting Started

To use the scripts in this repository, you'll need:

1. A Spotify Developer account. Create one at [Spotify Developer](https://developer.spotify.com/).
2. Register your application to get your `Client ID` and `Client Secret`.
3. Set your application's redirect URI. A common choice for development is `http://localhost:8888/callback`.

For detailed setup instructions, including how to set up your environment variables (`SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, `SPOTIPY_REDIRECT_URI`), watch this helpful [YouTube tutorial](https://www.youtube.com/watch?v=3RGm4jALukM).

## Example: Sort Playlist by Artist Popularity

This example demonstrates how to sort a Spotify playlist by artist popularity and followers using the Spotipy library. This script fetches tracks from a given playlist, retrieves artist data, and creates a new playlist with tracks sorted based on the artist's popularity and follower count.

### Highlights

- **Fetching in Blocks**: The Spotify Web API limits requests to 100 items at a time. Our script smartly batches these requests to efficiently manage playlists with more than 100 tracks, ensuring comprehensive sorting without hitting request limits.
- **Comprehensive Sorting**: Tracks are sorted by artist popularity and followers, providing an insightful perspective on music curation.
- **Playlist Creation**: Post-sorting, a new playlist is generated in your account, preserving the original while offering a fresh listening experience.

### Usage

1. Make sure your Spotify Developer account is set up, and your environment variables are correctly configured.
2. Run the script and enter the playlist URL when prompted.
3. A new playlist, sorted by artist popularity and followers, will be created in your Spotify account.

### Features

- Fetch playlist tracks and artist data.
- Sort tracks by artist popularity.
- Create a new playlist with sorted tracks.

This repository will continue to grow with more examples showcasing the versatility of the Spotipy library.

