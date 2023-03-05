'''You are tasked to create three classes: a Song class, an Album class, and a Band class.

The Song class should receive a name (string), a length (float), and a single (bool) upon initialization.\
It has one method:
-	get_info()
o	Returns the information of the song in this format: "{song_name} - {song_length}"

The Album class should receive a name (string) upon initialization and might receive one or more songs.\
It also has instance attributes: published (False by default) and songs (an empty list). It has four methods:
-	add_song(song: Song)
o	Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
o	If the song is single, returns "Cannot add {song_name}. It's a single"
o	If the album is published, returns "Cannot add songs. Album is published."
o	If the song is already added, return "Song is already in the album."
-	remove_song(song_name: str)
o	Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."
o	If the song is not in the album, returns "Song is not in the album."
o	If the album is published, returns "Cannot remove songs. Album is published."

-	publish()
o	Publishes the album (set to True) and returns "Album {name} has been published."
o	If the album is published, returns "Album {name} is already published."
-	details()
o	Returns the information of the album, with the songs in it, in the format:
"Album {name}
 == {first_song_info}
 == {second_song_info}
 …
 == {n_song_info}"

The Band class should receive a name (string) upon initialization. It also has an attribute albums (an empty list).
The class has three methods:
-	add_album(album: Album)
o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
o	If the album is already added, returns "Band {band_name} already has {album_name} in their library."
-	remove_album(album_name: str)
o	Removes the album from the collection and returns "Album {name} has been removed."
o	If the album is published, returns "Album has been published. It cannot be removed."
o	If the album is not in the collection, returns "Album {name} is not found."
-	details()
o	Returns the information of the band, with their albums, in this format:
"Band {name}
 {album details}
 ...
 {album details}"
'''

from typing import Tuple, List
from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs: List[Song] = list(*songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        [result.append(f"== {s.get_info()}") for s in self.songs]

        return "\n".join(result)
