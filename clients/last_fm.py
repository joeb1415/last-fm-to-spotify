import time

from pylast import md5, LastFMNetwork, User


class LastFMClient:
    def __init__(self):
        self.last_fm = None

    def login(self, api_key, api_secret, username, password):
        password_hash = md5(password)
        self.last_fm = LastFMNetwork(
            api_key=api_key,
            api_secret=api_secret,
            username=username,
            password_hash=password_hash,
        )

    def get_played_tracks(self, username, begin_time, end_time):
        begin_seconds = int(time.mktime(begin_time))
        end_seconds = int(time.mktime(end_time))

        user = User(user_name=username, network=self.last_fm)
        played_tracks = user.get_recent_tracks(limit=999, time_from=begin_seconds, time_to=end_seconds)
        played_tracks.reverse()

        return played_tracks

    @staticmethod
    def get_artist_title_searches(played_tracks):
        artist_title_searches = []
        for played_track in played_tracks:
            title = played_track.track.title
            artist = played_track.track.artist
            track_item = " ".join((str(artist), str(title))).lower()

            artist_title_searches.append(track_item)

        return artist_title_searches
