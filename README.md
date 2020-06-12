# last-fm-to-spotify
Create Spotify playlist from Last.fm scrobble playback history for a given time range

## Setup

### Last.fm

Create API account at https://www.last.fm/api/account/create 
Copy down your API key and secret as you can't access it again.

### Spotify

Set up a new application at https://developer.spotify.com/dashboard/applications
Include a Redirect URI. This can be any valid URL. 
Note client ID and secret. 

### Local

#### Set up environment

```bash
$ pyenv install 3.6.8
$ pyenv virtualenv 3.6.8 last-fm-to-spotify
$ pyenv local last-fm-to-spotify
(last-fm-to-spotify)$ poetry install
```

#### Run the script

```bash
(last-fm-to-spotify)$ python main.py
Last.fm API Key: 340979c3c50a6cb70555500446ebddf6
Last.fm API Secret: 41b6e57ae80c197337ed8d32fae65753
Last.fm Username: joeb1415
Last.fm Password: ***.
Begin time as `yyyy-mm-dd hh:mm:ss`: 2020-06-07 08:00:00
End time as `yyyy-mm-dd hh:mm:ss`: 2020-06-07 11:15:00
Spotify username: bryan.joe
Spotify client ID: 7ae8d91c250c46b48a6466098e29a37e
Spotify client secret: 8e868d78fbdd4351a6adf7fc17e3f061
Spotify redirect URI: https://github.com/joeb1415/last-fm-to-spotify
Enter the URL you were redirected to: https://github.com/joeb1415/last-fm-to-spotify?code=some_long_code [enter full URL from browser here]
Playlist name: my_playlist_name
99 tracks have been added to my_playlist_name.
```
