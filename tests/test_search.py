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