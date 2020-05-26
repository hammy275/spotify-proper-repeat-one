import spotipy
import spotipy.util as util
import os
import json
from time import sleep
import copy

scopes = ["user-read-playback-state", "user-modify-playback-state", "user-read-currently-playing"]
scope = ",".join(scopes)

username = os.getenv("SPOTIPY_USERNAME")
if username is None:
    username = input("Please enter your Spotify username: ")
    print("For future usage: If you configure this as an environment variable, you won't have to enter it ever again!")
print("Authenticating...")
token = util.prompt_for_user_token(username, scope)
print("Authenticated!")
client = spotipy.Spotify(auth=token)

print("Starting up...")
old_state = client.current_playback()
while old_state is None:
    sleep(5)
    old_state = client.current_playback()
sleep(5)
print("Startup complete!")
while True:
    new_state = client.current_playback()
    while new_state is None:
        sleep(5)
        new_state = client.current_playback()
    if old_state["repeat_state"] == "track" and new_state["repeat_state"] == "context" and new_state["progress_ms"] < 6000:
        print("Caught what's most likely Spotify doing its repeat switch! Switching it back...")
        client.repeat("track")
        new_state["repeat_state"] = "track"
    old_state = copy.deepcopy(new_state)
    sleep(5)
