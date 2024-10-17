"""Dessa Shapiro"""

class Time:
    __slots__ = ['hours', 'minutes', 'seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Song:
    __slots__ = ["title", "artist", "duration"]
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    __slots__ = ["title", "artist", "tracks", "total_time"]
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []
        self.total_time = 0

def add_song(song, album):
    album.tracks.append(song)
    album.total_time += song.duration


def get_time(time):
    return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)

def album_info(album):
    print(album.name)
    print(album.artist)
    print(album.tracks)
    print(album.total_time)
    


def main():
    song_one = Song("freefall", "Rainbow Kitten Suprize", "3:25")
    song_two = Song("Cocaine Jesus", "Rainbow Kitten Suprize", "3:40")
    song_three = Song("Love", "Rainbow Kitten Suprize", "2:45")
    album = Album("I donna Man", "Rainbow Kitten Suprize")
    add_song(song_one, album)
    add_song(song_two, album)
    add_song(song_three, album)
    album_info(album, album)
    
    #get_time(20)

if __name__ == "__main__":
    main()