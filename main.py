import utils
from pywebio.input import input
from pywebio.output import put_text


def main():
    while True:
        city = input("City: ")
        current_weather = utils.get_weather_info(city)
        put_text(f"Температура у {city}: {current_weather['temperature']}")

main()

