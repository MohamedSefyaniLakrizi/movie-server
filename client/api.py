import requests
from config import SERVER_URL, MAX_PAGES_PER_YEAR, MOVIES_PER_PAGE
from auth import authenticate

def fetch_movies_by_year(token, year):
    # Set authorization header
    headers = {"Authorization": f"Bearer {token}"}
    
    # Binary search to find highest valid page
    left = 1
    right = MAX_PAGES_PER_YEAR
    last_valid_page = -1
    last_page_data = []
    
    while left <= right:
        mid = (left + right) // 2
        url = f"{SERVER_URL}/api/movies/{year}/{mid}"
        response = requests.get(url, headers=headers)
        
        # Handle token expiration
        if response.status_code == 401:
            token = authenticate()
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(url, headers=headers)
            
        # Adjust search range based on response
        if response.status_code == 404:
            right = mid - 1  # Page doesn't exist, search lower
        elif response.status_code == 200:
            data = response.json()
            if data:  # Page has movies
                last_valid_page = mid
                last_page_data = data
                left = mid + 1  # Search for higher pages
            else:  # Page exists but is empty
                right = mid - 1
        else:
            raise Exception(f"Failed to fetch movies: {response.status_code} {response.text}")
    
    # Return 0 if no movies found
    if last_valid_page == -1:
        return 0

    # Calculate total movies
    movies_on_last_page = len(last_page_data)
    total_movies = (last_valid_page - 1) * MOVIES_PER_PAGE + movies_on_last_page
    return total_movies
