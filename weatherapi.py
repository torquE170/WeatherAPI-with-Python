from pprint import pprint
import requests
import api_keys  # create your api_keys file and create appropriate variables with the API key from your account
from datetime import datetime


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

print("Weather from https://www.weatherapi.com")
query_made = False
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
    print(option_1)
    print(option_2)
    print("3 - Make a new query")
    print()
    print("0 - Exit")
    while True:
        try:
            option = int(input(">> "))
            break
        except ValueError:
            print(">> Enter a valid number")
            continue
    if option == 1:
        if not query_made:
            continue
        print(f"Location: {response.json()['location']['country']}, {response.json()['location']['name']}, {response.json()['location']['region']}")
        print(f"Right now is {response.json()['current']['condition']['text']}, and it feels like {response.json()['current']['feelslike_c']}ºC")
        print(f"Temperature: {response.json()['current']['temp_c']}ºC, Humidity: {response.json()['current']['humidity']}RH"
              f"{f", Precipitation: {response.json()['current']['precip_mm']}mm" if response.json()['current']['precip_mm'] != 0 else ""}")
        print(f"Wind speed: {response.json()['current']['wind_kph']}km/h, Wind direction: {response.json()['current']['wind_dir']}, {response.json()['current']['wind_degree']}º")
        print()
    elif option == 2:
        if not query_made:
            continue
        for day in response.json()['forecast']['forecastday']:
            this_date = day['date']
            year, month, day_number = this_date.split("-")
            said_date = datetime.strptime(f"{year}{month}{day_number}", "%Y%m%d").date()
            day_string = said_date.strftime("%A")
            print(f"Location: {response.json()['location']['country']}, {response.json()['location']['name']}, {response.json()['location']['region']}")
            print(f"Date: {day['date']}, {day_string}, Average humidity: {day['day']['avghumidity']}"
                  f"{f", Precipitation: {day['day']['totalprecip_mm']}mm" if day['day']['totalprecip_mm'] != 0 else ""}")
            print(f"Sunrise: {day['astro']['sunrise']}, Sunset: {day['astro']['sunset']}")
            for hour in range(len(day['hour'])):
                print(f"[{hour:>02}:00] Temp: {day['hour'][hour]['temp_c']:>5.1f}ºC "
                      f"Wind: {day['hour'][hour]['wind_kph']:>5.1f}km/h - "
                      f"{day['hour'][hour]['wind_dir']:>4s}, "
                      f"Humidity: {day['hour'][hour]['humidity']:>3}"
                      f"{f", Precipitation: {day['hour'][hour]['precip_mm']}mm" if day['hour'][hour]['precip_mm'] != 0 else ""} ")
            print()
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
                valid_entry = True
            elif days.strip() == "":
                days = ""
                valid_entry = True
            break

        if q_param != "":
            q_param = f"q={q_param.lower()}"

        if int(days) > 7:
            days = "7"
        elif int(days) < 2:
            days = ""
        if days == "":
            days_param = ""
        else:
            days_param = f"days={days}"

        url_with_param = (url + f"{"?" if days_param != "" or q_param != "" else ""}" +
                          q_param + f"{"&" if days_param != "" else ""}" + days_param)

        query_made = True
        # print(url_with_param)
        response = requests.post(url_with_param, headers=headers)
        # pprint(response.json())
        print()

    elif option == 0:
        break

    else:
        print(">> Enter a valid menu option")
        print()