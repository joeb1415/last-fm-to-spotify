from spotipy import prompt_for_user_token, SpotifyClientCredentials, Spotify


SCOPE = 'playlist-modify-public'


class SpotifyClient:
    def __init__(self):
        self.spotify = None

    def login(self, username, client_id, client_secret, redirect_uri):
        token = prompt_for_user_token(
            username=username,
            scope=SCOPE,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
        )
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        spotify = Spotify(auth=token, client_credentials_manager=client_credentials_manager)
        spotify.trace = False

        self.spotify = spotify

    @staticmethod
    def normalize_search(search_str):
        words = search_str.lower().split(" ")
        remove_words = ["the", "a", "an"]
        filtered_words = list(filter(lambda x: x not in remove_words, words))
        normalized_search = " ".join(filtered_words)

        return normalized_search

    def _get_track_id(self, artist_title):
        normalized_search = self.normalize_search(artist_title)
        result = self.spotify.search(q=normalized_search)

        for track_item in result["tracks"]["items"]:
            track = track_item["name"]
            artist = track_item["album"]["artists"][0]["name"]
            if track.lower() in artist_title.lower() and artist.lower() in artist_title.lower():
                return track_item["id"]

    def get_track_ids(self, artist_title_searches):
        track_ids = []
        for artist_title in artist_title_searches:
            track_id = self._get_track_id(artist_title=artist_title)
            if track_id:
                track_ids.append(track_id)

        return track_ids

    def create_playlist(self, username, name):
        playlist = self.spotify.user_playlist_create(user=username, name=name)

        return playlist

    def add_tracks_to_playlist(self, username, playlist, track_ids):
        self.spotify.user_playlist_add_tracks(user=username, playlist_id=playlist["id"], tracks=track_ids)
