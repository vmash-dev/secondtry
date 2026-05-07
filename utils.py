import requests
import constants
import config

def get_weather_info(city: str) -> dict:
    params = {
        "q": city,
        "appid": config.API_KEY,
        "units": "metric",
    }
    response = requests.get(constants.OPEN_WEATHER_API_URL, params=params)
    response_json = response.json()
    print(response.url, response_json)
    return {}



get_weather_info("Одеса")


