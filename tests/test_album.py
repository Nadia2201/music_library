from lib.album import *

"""
Constructs with id, title, release_year, artist_id
"""

def test_constructs_correct_fileds():
    album = Album('Bossanova', 1990, 1)
    assert album.title == 'Bossanova'
    assert album.release_year == 1990
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album('Bossanova', 1990, 1)
    assert str(album) == "Album(Bossanova, 1990, 1)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album('Bossanova', 1990, 1)
    album2 = Album('Bossanova', 1990, 1)
    assert album1 == album2