# Movie Server

This server serves movie lists via a REST API.

## Solution

### Part 1: Fix the Server

The repository included a Makefile that had build issues. The problem was **incorrect indentation**. the Makefile didn't have indentation, which caused the build commands to fail. After fixing the indentation, the server compiled and ran correctly.

### Part 2: Python Client Implementation

A Python command-line client was developed with the following structure:

- **`client.py`** - Main entry point, handles command-line arguments and coordinates authentication/API calls
- **`auth.py`** - Handles authentication with the server and token management
- **`api.py`** - Contains the core logic for fetching movie counts using binary search
- **`config.py`** - Centralized configuration file for server URL, credentials, and limits

This structure make the client side clear and easily maintainable by putting all important variables inside the config and requirements inside the requirements.txt file. It needs to be noted that the linear approach of incrementing the movies number in each page was very slow, so I came up with a binary search solution that is much more efficient and reduces the number of API calls and reduces the complexity from O(n) to O(log(n)).

#### Usage

```bash
# Install dependencies
pip install -r client/requirements.txt

# Run client with one or more years
python client/client.py 1999 2000 2001
```

The client outputs the number of films for each requested year:

```
1999: 4703 films
2000: 4619 films
2001: 4329 films
```

## API Endpoints

## API Endpoints

```
The following endpoints are available:

POST /api/auth
	This endpoint allows users to authenticate themselves with the server. Accepts a JSON body with the following format:
		{"username": "USERNAME", "password": "PASSWORD"}

	On a success, the endpoint will return a JSON packet with the following format:
		{"bearer": "TOKEN", "timeout": TOKEN_LIFETIME}

GET /api/movies/$YEAR/$PAGE
	This endpoint requires the bearer token passed in the Authorization header. Will return a JSON list of upto 10 movies.
```

## Server Usage

=====

```
  -port uint
    	port to listen on (default 8080)
```
