# Ping Pong Movie Hub

**Ping Pong Movie Hub** is a Python application built using `CustomTkinter` that allows users to search for movies, view posters, and read movie overviews. It fetches data from The Movie Database (TMDb) API and provides links to video streaming servers.

## Features

- **Search for Movies**: Users can search for movies by name.
- **Movie Details**: Display movie title, release date, poster, and overview.
- **Pagination**: Navigate through the movie results with "Next" and "Previous" buttons.
- **Streaming Links**: Provides two servers (Server 1 and Server 2) to watch the movie online.
  
## Requirements

- Python 3.12
  
## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/pingpong-movie-hub.git
    ```

2. Install required dependencies:

    ```bash
    pipip install -r requirements.txt
    ```

3. Get an API key from [The Movie Database](https://www.themoviedb.org/) and place it in the `key.py` file.

4. Run the application:

    ```bash
    python app.py
    ```

## How to Use

1. Enter a movie name in the search bar and click the "SEARCH" button.
2. The application will display the movie's poster, release date, and overview.
3. Use the "Next" and "Prev" buttons to navigate through movie results.
4. Click on "Server 1" or "Server 2" to watch the movie online.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
