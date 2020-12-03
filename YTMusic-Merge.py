from ytmusicapi import YTMusic
import os
import sys

playlist_id = os.environ["YT_PLAYLIST"]
limit = sys.maxsize

ytmusic = YTMusic("auth.json")

songs_library = ytmusic.get_library_songs(
    limit=limit, validate_responses=True
)
songs_local = ytmusic.get_library_upload_songs(limit=limit)
songs = songs_library + songs_local
songs = dict((s["videoId"], s["title"]) for s in songs)

playlist_songs = ytmusic.get_playlist(playlistId=playlist_id, limit=0)["tracks"]
playlist_songs = dict((p["videoId"], p) for p in playlist_songs)

remove_songs, add_songs = [], []
for p in playlist_songs:
    if p not in songs:
        remove_songs.append(p)

for s in songs:
    if s not in playlist_songs:
        add_songs.append(s)

if remove_songs and songs_library:
    print("------------------------------")
    print("[Remove Songs]")
    remove_title = [playlist_songs[s]["title"] for s in remove_songs]
    remove_songs = [
        {
            "videoId": playlist_songs[s]["videoId"],
            "setVideoId": playlist_songs[s]["setVideoId"],
        }
        for s in remove_songs
    ]
    print("\n".join(remove_title))
    ytmusic.remove_playlist_items(playlistId=playlist_id, videos=remove_songs)

if add_songs:
    print("------------------------------")
    print("[Add Songs]")
    add_title = [songs[s] for s in add_songs]
    print("\n".join(add_title))
    ytmusic.add_playlist_items(playlistId=playlist_id, videoIds=add_songs)

print("------------------------------")
print("Done!")
