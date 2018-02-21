

class Song:
    """Class to represent the song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero

    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method
        :param title: Initializes the 'title' attribute
        :param artist: At artist object representing the song's creator
        :param duration (Optional(int)): Initial value for the 'duration' attribute
         Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album using it's track list
        name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist responsible for the album
        tracks (List(Song)): A list of the songs of the album

        Methods:
            addSong: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various artists")
        else:
            self.artist = artist
        self.tracks  = []

    def add_song(self, song, position = None):
        """Adds a song to the track list

        Args:
            song(Song): A song to add
            position (Optional{int)): Position, otherwise song will be added to the end of the list
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    Attributes
        name (str): The name of the artist
        albums (List(Album)): A list of the albums by this artist.
        The list includes only those albums in this collection, it is not an exhaustive list
        of the artists's published albums

    Methods:
        add_album: Use to add a new album to the artist's album list
    """

    def __init__(self, name):
        self.name = name
        self.albums= []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album (Album): Album object to add to the list.
            If the album is already present. It will not be added again
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                #we have just found a new album for the current artist
                #store the current album in the artist's collection and then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            #create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        #After reading gthe last line of the text file, we will have an artist that hasnt be stored
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_checkfile(artist_list):
    #create a check file from the object data for comparison with original file
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)

if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)