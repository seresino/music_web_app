import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist_repository import *
from lib.artist import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route('/albums', methods = ['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection) 
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(album)
    return ""

@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection) 
    albums = repository.all()
    album_strings = [f"Album({album.id}, {album.title}, {album.release_year}, {album.artist_id})" for album in albums]
    result = ", ".join(album_strings)
    return result

@app.route('/albums/<int:id>', methods = ['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return str(album)

@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return "Album deleted successfully"

@app.route('/artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artists_strings = [f"{artist.name}" for artist in artists]
    result = ", ".join(artists_strings)
    return result

@app.route('/artists', methods = ['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection) 
    artist = Artist(None, request.form['name'], request.form['genre'], [])
    repository.create(artist)
    return ""

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# @app.route('/artists', methods = ['POST'])
# def create_artist():
#     if ('name' not in request.form) or ('genre' not in request.form):
#         response = make_response("Bad Request - Please provide a name and genre!")
#         response.status_code = 400
#         print("if path")
#         print(request.form['name'], request.form['genre'])
#         return response

#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist = Artist(None, request.form['name'], request.form['genre'])
#     repository.create(artist)
#     return "Artists added successfully"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

