# Spotify API Automation

This project automates testing of the **Spotify Web API** using Python and `pytest`. It demonstrates authentication, API requests, logging, and test automation.

---

## Project Structure
spotify_api_automation/
├─ src/
│ ├─ api_client.py # Handles Spotify authentication and API requests
│ └─ config.py # Stores BASE_URL, CLIENT_ID, CLIENT_SECRET
├─ tests/
│ ├─ init.py
│ ├─ test_search.py # 2 tests for /search endpoint
│ └─ test_artists.py # 4 tests for /artists endpoint
├─ logs/ # Stores logs and HTML reports
├─ requirements.txt # Python dependencies
├─ pytest.ini # Pytest configuration
└─ README.md # This file
---

## Setup

1. Clone the repository and enter the folder:

```powershell
git clone https://github.com/amineabdsattar/Yassir_api_automation.git
cd Yassir_api_automation

2. Create and activate a virtual environment

```powershell
python -m venv venv
# Windows
venv\Scripts\Activate

3. install packages

```powershell
python -m pip install -r requirements.txt

4. Update your Spotify credentials

Edit the file src/config.py and add your own credentials from
https://developer.spotify.com/dashboard
```powershell
BASE_URL = "https://api.spotify.com/v1"
CLIENT_ID = "<your_client_id>"
CLIENT_SECRET = "<your_client_secret>"

5. run tests

Run all tests with verbose output
```powershell
python -m pytest -v

generate HTML test report
python -m pytest --html=logs/report.html --self-contained-html -v

6. test cases

Search Endpoint (tests/test_search.py)
 -Search for an artist → expect 200 OK
 -Search for a track → expect 200 OK

Artists Endpoint (tests/test_artists.py)
 -Get artist info by valid ID → expect 200 OK
 -Get artist info by invalid ID → expect 400 Bad Request
 -Search for an artist → expect 200 OK
 -Search for a track → expect 200 OK

 