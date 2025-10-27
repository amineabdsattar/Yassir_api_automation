from src.api_client import SpotifyClient

client = SpotifyClient()

def test_search_artist_success():
    """Test searching for an artist returns results"""
    response = client.get("/search", params={"q": "Coldplay", "type": "artist"})
    assert response.status_code == 200
    assert "artists" in response.json()

def test_search_track_success():
    """Test searching for a track returns results"""
    response = client.get("/search", params={"q": "Yellow", "type": "track"})
    assert response.status_code == 200
    assert "tracks" in response.json()
from src.api_client import SpotifyClient

client = SpotifyClient()

def test_artist_info_success():
    """Test fetching artist info by valid artist ID"""
    # Example artist ID
    artist_id = "4gzpq5DPGxSnKTe4SA8HAU"
    response = client.get(f"/artists/{artist_id}")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data

def test_artist_invalid_id():
    """Test fetching artist info with invalid ID returns 400"""
    artist_id = "medaminebenabdsattar"
    response = client.get(f"/artists/{artist_id}")
    assert response.status_code == 400