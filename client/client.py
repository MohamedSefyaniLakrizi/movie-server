import sys
from auth import authenticate
from api import fetch_movies_by_year

def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 client.py <year1> [<year2> ...]")
        sys.exit(1)

    years = sys.argv[1:]
    
    # Authenticate with server
    try:
        token = authenticate()
    except Exception as e:
        print(f"Authentication error: {e}")
        sys.exit(1)

    # Fetch movie counts for each year
    for year in years:
        try:
            num_movies = fetch_movies_by_year(token, year)
            print(f"{year}: {num_movies} movies")
        except Exception as e:
            print(f"{year}: Error - {e}")

if __name__ == "__main__":
    main()
