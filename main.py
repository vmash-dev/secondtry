import utils
from pywebio.input import input
from pywebio.output import put_text


def main():
    # count = 0
    while True:
        city = input("City: ")
        current_weather = utils.get_weather_info(city)
        put_text(f"Температура у {city}: {current_weather['temperature']}")
        # count = count + 1
        # print(count)
        print(current_weather)

main()

