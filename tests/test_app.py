# Tests for your routes go here
"""
When I call GET /albums 
All albums are returned
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1), Album(2, Waterloo, 1974, 2), Album(3, Lover, 2019, 3), Album(4, Baltimore, 1978, 4)"

"""
When I call GET /albums/<id>
The album with the correspdonding id is returned
"""
def test_get_album(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    get_response = web_client.get("/albums/3")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Album(3, Lover, 2019, 3)"

"""
When I call POST /albums with album info
That album is now in the list returned by GET /albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/albums", data =
    {
        'title': 'Little Girl Blue',
        'release_year': '1959',
        'artist_id': 4
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1), Album(2, Waterloo, 1974, 2), Album(3, Lover, 2019, 3), Album(4, Baltimore, 1978, 4), Album(5, Little Girl Blue, 1959, 4)"


"""
When I call GET /artists
All artists are returned
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
When I call POST /artists with artist info name = 'Wild Nothing' and genre 'Indie'
That artist is now in the list returned by GET /artists
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")

    post_response = web_client.post("/artists", data = 
    {
        'name': 'Wild Nothing',
        'genre': 'Indie'
    })

    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild Nothing"

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
