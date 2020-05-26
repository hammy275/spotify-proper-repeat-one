# spotify-proper-repeat-one

A very small Python program that makes it so when you go to another song with the repeat mode set to "only this song", it will correct Spotify's automatic change to "repeat this playlist/album/whatever" back to "repeat this song.

## Setup (for Linux and macOS systems with Python 3.7 or greater)

1. `pip3 install -r requirements.txt`
2. Create a Client ID here: https://developer.spotify.com/dashboard/applications with any name and any description and any uses
3. Edit the settings for the Client ID/app, and add `http://localhost/` in the "Redirect URIs" section.
4. Set the following environment variables:
   * `SPOTIPY_USERNAME`: Your Spotify username.
   * `SPOTIPY_CLIENT_ID`: The Client ID as shown in the Client ID/app.
   * `SPOTIPY_CLIENT_SECRET`: The Client Secret as shown in the Client ID/app.
   * `SPOTIPY_CLIENT_URI`: Should be set to `http://localhost/`
5. `python3 main.py`
   
## How It Works

Simply put, it will constantly look (every 5 seconds) to see if 5 seconds ago, you were repeating a song, but are now repeating a playlist/whatever and the song you're playing is less than 6 seconds through. If so, it probably got auto-changed by Spotify, and we should change it back.

## Limitations

Because of how this program works, you shouldn't change from "repeat only this song" to "repeat this playlist or whatever else" during the first six seconds of a song.