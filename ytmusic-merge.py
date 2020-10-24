from ytmusicapi import YTMusic
import os

playlist_id = os.environ['YT_PLAYLIST']

ytmusic = YTMusic('auth.json')

songs = ytmusic.get_library_songs(limit=0, validate_responses=True) + ytmusic.get_library_upload_songs(limit=0)
songs = [songs['videoId'] for songs in songs]

playlist_songs = ytmusic.get_playlist(playlistId=playlist_id, limit=0)['tracks']
playlist_songs = [playlist_songs['videoId'] for p in playlist_songs]

remove_songs, add_songs = [], []
for p in playlistSongs:
    if p not in songs:
        remove_songs.append(p)

for s in songs:
    if s not in playlistSongs:
        add_songs.append(s)

if remove_songs:
    print('------------------------------')
    print('Remove Songs:',remove_songs)
    ytmusic.remove_playlist_items(playlistId=playlistId, videos=remove_songs)

if add_songs:
    print('------------------------------')
    print('Add Songs:', add_songs)
    ytmusic.add_playlist_items(playlistId=playlistId, videoIds=add_songs)

print('Done!')