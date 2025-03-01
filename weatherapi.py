from pprint import pprint
import requests
import api_keys  # create your api_keys file and create appropriate variables with the API key from your account
from datetime import datetime
import os
import sys

def clear():
    if "win" in sys.platform:
        os.system("cls")
    elif "linux" in sys.platform:
        os.system("clear")

url = f"https://api.weatherapi.com/v1/forecast.json"
# current.json - for current weather
# forecast.json - for the forecast for the current day, or multiple days with key days=value
# set ?q=bulk for multiple locations in one query and do POST instead of GET

headers = {
    "key": api_keys.weather_api_key
}

#  use multiple locations when q is set to bulk
body = {
    "locations": [
        {
            "q": "Iasi",  # required
            "custom_id": "town01"  # optional
        },
        {
            "q": "Bucuresti",
            "custom_id": "town02"
        },
        {
            "q": "Suceava",
            "custom_id": "town03"
        }
    ]
}

clear()
query_made = False
wrong_option = False
option = -1
while option != 0:
    if query_made:
        option_1 = f"1 - Current weather for {response.json()['location']['country']}, {response.json()['location']['name']}, {response.json()['location']['region']}"
    else:
        option_1 = "1 - Current weather - no query has been made"
    if query_made:
        if days != "":
            option_2 = f"2 - Forecast for {days} days"
        else:
            option_2 = f"2 - Forecast for the day"
    else:
        option_2 = "2 - Forecast for - no query has been made"
    print("Weather from https://www.weatherapi.com")
    print(option_1)
    print(option_2)
    print("3 - Make a new query")
    print()
    print("0 - Exit")
    if wrong_option:
        print(">>")
        print(">> Enter a valid menu option")
        wrong_option = False
    while True:
        try:
            option = int(input(">> "))
            clear()
            break
        except ValueError:
            print(">> Enter a valid number")
            continue
    if option == 1:
        if not query_made:
            continue
        print(f"Location: {response.json()['location']['country']}, {response.json()['location']['name']}, {response.json()['location']['region']}")
        print(f"Right now is {response.json()['current']['condition']['text']}, and it feels like {response.json()['current']['feelslike_c']}ºC")
        print(f"Temperature: {response.json()['current']['temp_c']}ºC, Humidity: {response.json()['current']['humidity']}RH", end = "")
        print(f", Precipitation: {response.json()['current']['precip_mm']}mm" if response.json()['current']['precip_mm'] != 0 else "")
        print(f"Wind speed: {response.json()['current']['wind_kph']}km/h, Wind direction: {response.json()['current']['wind_dir']}, {response.json()['current']['wind_degree']}º")
        print()
    elif option == 2:
        if not query_made:
            continue
        forcast_list = response.json()['forecast']['forecastday']
        day = 0
        while True:
            this_date = forcast_list[day]['date']
            year, month, day_number = this_date.split("-")
            said_date = datetime.strptime(f"{year}{month}{day_number}", "%Y%m%d").date()
            day_string = said_date.strftime("%A")
            print(f"Location: {response.json()['location']['country']}, {response.json()['location']['name']}, {response.json()['location']['region']}")
            print(f"Date: {forcast_list[day]['date']}, {day_string}, Average humidity: {forcast_list[day]['day']['avghumidity']}", end="")
            print(f", Precipitation: {forcast_list[day]['day']['totalprecip_mm']}mm" if forcast_list[day]['day']['totalprecip_mm'] != 0 else "")
            print(f"Sunrise: {forcast_list[day]['astro']['sunrise']}, Sunset: {forcast_list[day]['astro']['sunset']}")
            for hour in range(len(forcast_list[day]['hour'])):
                print(f"[{hour:>02}:00] Temp: {forcast_list[day]['hour'][hour]['temp_c']:>5.1f}ºC "
                      f"Wind: {forcast_list[day]['hour'][hour]['wind_kph']:>5.1f}km/h - "
                      f"{forcast_list[day]['hour'][hour]['wind_dir']:>4s}, "
                      f"Humidity: {forcast_list[day]['hour'][hour]['humidity']:>3}", end="")
                print(f", Precipitation: {forcast_list[day]['hour'][hour]['precip_mm']}mm" if forcast_list[day]['hour'][hour]['precip_mm'] != 0 else "")
            print()
            option_days = input("(Next/Previous/Quit) >> ")
            clear()
            if option_days.lower() == 'n' or option_days.lower() == 'next':
                if day < len(forcast_list) - 1:
                    day += 1
            if option_days.lower() == 'p' or option_days.lower() == 'previous':
                if day > 0:
                    day -= 1
            if option_days.lower() == 'q' or option_days.lower() == 'quit':
                break
        print()
    elif option == 3:
        valid_entry = False
        while not valid_entry:
            q_param = input("Enter your town: ")
            if q_param.strip() != "":
                break

        valid_entry = False
        while not valid_entry:
            days = input("Forecast days: ")
            if days.isnumeric():
                days = int(days)
                if days > 7:
                    days = "7"
                elif days < 2:
                    days = ""
                days = str(days)
                valid_entry = True
            elif days.strip() == "":
                days = ""
                valid_entry = True
            break

        days_param = f"days={days}"

        if q_param != "":
            q_param = f"q={q_param.lower()}"
        question_mark = "?" if days_param != "" or q_param != "" else ""
        ampercent = "&" if days_param != "" else ""
        url_with_param = url + question_mark + q_param + ampercent + days_param

        query_made = True
        # print(url_with_param)
        response = requests.post(url_with_param, headers=headers)
        # pprint(response.json())
        clear()

    elif option == 0:
        break

    else:
        wrong_option = True
