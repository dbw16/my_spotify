import json
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "3f41664239824c288f53bb2231903ef7"
client_secret = os.environ['CLIENT_SECRET']

redirect_uri = "http://127.0.0.1:9090"  # declared in the spotify app

sp_client = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read",
    )
)


def get_saved_songs():
    tracks = []
    limit, off_set = 50, 0
    results = sp_client.current_user_saved_tracks(limit=50, offset=off_set)
    while results["next"]:
        for item in results["items"]:
            tracks.append(item["track"])
        off_set += 50
        results = sp_client.current_user_saved_tracks(limit=50, offset=off_set)

    return tracks


def generate_json(tracks):
    with open("tracks.json", "w+") as f:
        json.dump(tracks, f, indent=3)


def generate_text(tracks):
    with open("tracks.txt", "w+") as f:
        for i, track in enumerate(tracks):
            f.write(f"{i}: {track['name']} by {track['artists'][0]['name']}\n")


def main():
    print("starting")
    exit(1)
    tracks = get_saved_songs()
    generate_json(tracks)
    generate_text(tracks)


if __name__ == "__main__":
    main()
