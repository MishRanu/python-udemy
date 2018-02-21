import os
import fnmatch


def find_songs_extension(start, artist_name, extension):
    for path, directories, files in os.walk(start):
        for file in files:
            match_string = "*".join((artist_name, extension))
            if fnmatch.fnmatch(file, match_string):
                file_path = os.path.join(path, file)
                yield file_path
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, album_files in os.walk(subdir):
                for album_file in album_files:
                    yield os.path.join(album_path, album_file)

                # for album in albums:
                #     song_path = os.path.join(album_path, album)
                #     for song in os.listdir(song_path):
                #         yield song

song_list = find_songs_extension("music", "Aerosmith", ".emp3")

for new_song in song_list:
    print(new_song)

def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


# there has to be a way to get a list of songs on the albums
def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):   #We want the path and not the name of the album
            yield song
