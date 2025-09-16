# Movie Server

This server serves movie lists via a REST API.

#### Usage

```bash
# Runs the container and exectutes the python client
sudo docker-compose run --rm client python3 client.py 1999 2000 2001
```

The year is taken as an input and is seperated by a space

```bash
# example output
1999: 4703 movies
2000: 4619 movies
2001: 5181 movies
```

## Solution

### Part 1: Fix the Server

Language used: Go

The repository included a Makefile that had build issues. The problem was **incorrect indentation**. the Makefile didn't have indentation, which caused the build commands to fail. After fixing the indentation, the server compiled and ran correctly.

### Part 2: Write a client

Language used: Python

A Python command-line client was developed with the following structure:

- **`client.py`** - Main entry point, handles command-line arguments and coordinates authentication/API calls
- **`auth.py`** - Handles authentication with the server and token management
- **`api.py`** - Contains the core logic for fetching movie counts using binary search
- **`config.py`** - Centralized configuration file for server URL, credentials, and limits

This structure make the client side clear and easily maintainable by putting all important variables inside the config and requirements inside the requirements.txt file. It needs to be noted that the linear approach of incrementing the movies number in each page was very slow, so I came up with a binary search solution that is much more efficient and reduces the number of API calls and reduces the complexity from O(n) to O(log(n)).

### Part 3: Containerize

Container solution used: Docker

I used docker compose and exposed the port 8080 for the client to access it. I also added the server as a dependency to avoid any errors.
