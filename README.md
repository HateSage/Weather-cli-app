# Weather CLI

A command-line weather app written in Python. Takes a city name as input, fetches current conditions from the OpenWeatherMap API, and prints temperature, feels-like temperature, and conditions.

Built as a hands-on project to learn HTTP requests, JSON parsing, environment variables, and API error handling.

## Features

- Fetches live weather data from the OpenWeatherMap API
- Reads your API key from a `.env` file (never hardcoded)
- Handles common failure cases: invalid API key, city not found, network timeout, connection errors
- Simple command-line interface — just pass a city name

## Setup

1. Clone the repo and enter the folder:
   ```bash
   git clone <your-repo-url>
   cd weather-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

4. Create a `.env` file in the project folder:
   ```
   OWM_API_KEY=your_api_key_here
   ```

## Usage

```bash
python main.py Lagos
python main.py "New York"
```

Example output:
```
Weather in Lagos is: 28.5,feels like: 30.1
description: overcast clouds
```

## What this project covers

- Making HTTP requests with `requests`
- Reading and parsing JSON responses
- Authenticating with an API key
- Keeping secrets out of source code with environment variables (`python-dotenv`)
- Handling HTTP error codes (401, 404) and network failures (timeouts, connection errors)
- Building a command-line interface with `argparse`
- Reading and applying third-party API documentation

## License

MIT
