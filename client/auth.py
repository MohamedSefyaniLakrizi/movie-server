import requests
from config import SERVER_URL, USERNAME, PASSWORD

def authenticate():
    # Send authentication request to server
    url = f"{SERVER_URL}/api/auth"
    response = requests.post(url, json={"username": USERNAME, "password": PASSWORD})
    
    # Check for authentication failure
    if response.status_code != 200:
        raise Exception(f"Authentication failed: {response.text}")
        return None

    # Extract bearer token from response
    data = response.json()
    return data["bearer"]
