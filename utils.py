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
    # print(response.url, response_json)
    temperature = response_json["main"]["temp"]
    temperature_like = response_json["main"]["feels_like"]
    weather_main = response_json["weather"][0]["main"]
    weather_description = response_json["weather"][0]["description"]
    wind_speed = response_json["wind"]["speed"]
    return {
        "temperature": temperature,
        "temperature_like": temperature_like,
        "weather_main": weather_main,
        "weather_description": weather_description,
        "wind_speed": wind_speed,
    }

def write_logs():
    with open(constants.LOG_CSV_FILE_NAME, mode="a", encoding="utf-8") as file:
        data =







