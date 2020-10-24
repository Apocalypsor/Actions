from ytmusicapi import YTMusic
import os

playlist_id = os.environ['YT_PLAYLIST']

ytmusic = YTMusic('auth.json')

songs = ytmusic.get_library_songs(limit=0, validate_responses=True) + ytmusic.get_library_upload_songs(limit=0)
songs = [s['videoId'] for s in songs]

playlist_songs = ytmusic.get_playlist(playlistId=playlist_id, limit=0)['tracks']
playlist_songs_id = [p['videoId'] for p in playlist_songs]

remove_songs, add_songs = [], []
for p in playlist_songs:
    if p['videoId'] not in songs:
        remove_songs.append(p)

for s in songs:
    if s not in playlist_songs_id:
        add_songs.append(s)

if remove_songs:
    print('------------------------------')
    print('Remove Songs:',remove_songs)
    ytmusic.remove_playlist_items(playlistId=playlist_id, videos=remove_songs)

if add_songs:
    print('------------------------------')
    print('Add Songs:', add_songs)
    ytmusic.add_playlist_items(playlistId=playlist_id, videoIds=add_songs)

print('Done!')