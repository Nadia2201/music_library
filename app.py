from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.artist_repository import Artist
from lib.album_repository import Album


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")


class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
    user_input = input("""Welcome to the music library manager!
    
What would you like to do?
    1 - List all albums
    2 - List all artists
          
    Enter your choice:""")
# Retrieve all artists
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    if user_input == "1":
# List them out
        print ("Here is the list of artists:")
        for artist in artists:
            print(artist)
    elif user_input == "2":
        print ("Here is the list of albums:")
        for album in albums :
           print(album) 
    else:
        print("pick 1 or 2")     


if __name__ == '__main__':
    app = Application()
    app.run()

# album_repository = AlbumRepository(connection)
# albums = album_repository.all()
# for album in albums:
#     print(album)

# print(album_repository.find(1))    

# album_repository.create(Album(None, "Voyage", 2021, 2))
# albums = album_repository.all()
# for album in albums:
#     print(album)
    

    
