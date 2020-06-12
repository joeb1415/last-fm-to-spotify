import time
from getpass import getpass

from clients.last_fm import LastFMClient
from clients.spotify import SpotifyClient


last_fm_client = LastFMClient()

last_fm_api_key = input("Last.fm API Key: ")
last_fm_api_secret = input("Last.fm API Secret: ")
last_fm_username = input("Last.fm Username: ")
last_fm_password = getpass("Last.fm Password: ")

last_fm_client.login(
    api_key=last_fm_api_key,
    api_secret=last_fm_api_secret,
    username=last_fm_username,
    password=last_fm_password,
)

begin_time_str = input("Begin time as `yyyy-mm-dd hh:mm:ss`: ")
end_time_str = input("End time as `yyyy-mm-dd hh:mm:ss`: ")
begin_time = time.strptime(begin_time_str, "%Y-%m-%d %H:%M:%S")
end_time = time.strptime(end_time_str + "", "%Y-%m-%d %H:%M:%S")

played_tracks = last_fm_client.get_played_tracks(username=last_fm_username, begin_time=begin_time, end_time=end_time)
artist_title_searches = last_fm_client.get_artist_title_searches(played_tracks=played_tracks)

spotify_client = SpotifyClient()

spotify_username = input("Spotify username: ")
spotify_client_id = input("Spotify client ID: ")
spotify_client_secret = input("Spotify client secret: ")
spotify_redirect_uri = input("Spotify redirect URI: ")

spotify_client.login(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    username=spotify_username,
    redirect_uri=spotify_redirect_uri,
)
spotify_track_ids = spotify_client.get_track_ids(artist_title_searches=artist_title_searches)

spotify_playlist_name = input("Playlist name: ")

playlist = spotify_client.create_playlist(
    username=spotify_username,
    name=spotify_playlist_name,
)

for start_index in range(0, len(spotify_track_ids), 100):
    chunk_track_ids = spotify_track_ids[start_index : start_index + 100]

    spotify_client.add_tracks_to_playlist(
        username=spotify_username,
        playlist=playlist,
        track_ids=chunk_track_ids,
    )

print(f"{len(spotify_track_ids)} tracks have been added to {spotify_playlist_name}.")
