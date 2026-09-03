import os
import requests
import argparse
from dotenv import load_dotenv
import sys
load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city,units="metrics"):
    api_key = os.environ.get("OWM_API_KEY")
    if not api_key:
        print("Error while fetching your api key, please check your .env file to see if it exists")
        sys.exit(1)

    params = {"q":city,"appid":api_key,"units":units}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.Timeout:
        print("Error: Timeout occured while fecthing the city info,please try again")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Error: Connection failure,Try again")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Error occured {e}")
        sys.exit(1)

    if response.status_code == 404:
        print(f"{city} does not exist, please check and try again")
        sys.exit(1)
    elif response.status_code == 401:
        print("Bad request, please try again")
        sys.exit(1)
    elif response.status_code == 500:
        print("Error: internal server error")
        sys.exit(1)

    return response.json()

def format_weather(data):
    name = data['name']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    description = data['weather'][0]['description']
    return f"the temperature in {name} is: {temp},feels like: {feels_like}\ndescription: {description}"

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("city")
    args = parser.parse_args()
    data = get_weather(args.city)
    print(format_weather(data))


if __name__ == "__main__":
    main()