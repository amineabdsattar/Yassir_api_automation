import requests
import logging
from src.config import BASE_URL, CLIENT_ID, CLIENT_SECRET

# Configure logging
logging.basicConfig(
    filename="logs/api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SpotifyClient:
    def __init__(self):
        self.token = self.get_token()
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_token(self):
        """Obtain access token using Client Credentials Flow"""
        url = "https://accounts.spotify.com/api/token"
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
        response.raise_for_status()
        token = response.json().get("access_token")
        logging.info("Obtained access token")
        return token

    def get(self, endpoint, params=None):
        """Send GET request to Spotify API and log request/response"""
        url = f"{BASE_URL}{endpoint}"
        logging.info(f"GET Request: {url} | Params: {params}")
        response = requests.get(url, headers=self.headers, params=params)
        logging.info(f"Response: {response.status_code} | {response.text}")
        return response