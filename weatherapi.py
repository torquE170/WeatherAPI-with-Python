from pprint import pprint
import requests
import api_keys  # create your api_keys file and create apropriate variabiles with the API key from your account


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
    option = int(input(">> "))
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
            print(f"Location: {response.json()['location']['country']}, {response.json()['location']['name']}, {response.json()['location']['region']}")
            print(f"Date: {day['date']}, Average humidity: {day['day']['avghumidity']}"
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
        q_param = input("Enter your town: ")
        while True:
            try:
                days = int(input("Forecast days: "))
                break
            except ValueError:
                continue

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

    elif option == 0:
        break


#  ------------------------ current weather data -----------------------------
#  json['current']['condition']['text'] - text condition for current weather
#  json['current']['feelslike_c'] - feels like temp
#  json['current']['temp_c'] - temp
#  json['current']['wind_kph'] - wind speed
#  json['current']['wind_dir'] - wind direction
#  json['current']['wind_degree'] - exact wind direction
#  json['current']['pressure_mb'] - barometric pressure
#  json['current']['humidity'] - barometric pressure
#  json['current']['precip_mm'] - precipitation in mm

#  ---------------------------- location data ----------------------------------
#  json['location']['country']
#  json['location']['localtime']
#  json['location']['tz_id']
#  json['location']['name']
#  json['location']['region']

#  ------------------------ forecast weather data ------------------------------
#  json['forecast']['forecastday'][0-7]['date'] - date of forecast
#         dict      list of dict   day
#  json['forecast']['forecastday'][0-7]['day'] - forecast for the whole day
#  json['forecast']['forecastday'][0-7]['day']['mintemp_c']
#  json['forecast']['forecastday'][0-7]['day']['avgtemp_c']
#  json['forecast']['forecastday'][0-7]['day']['maxtemp_c']
#  json['forecast']['forecastday'][0-7]['day']['totalprecip_mm']
#  json['forecast']['forecastday'][0-7]['day']['daily_chance_of_rain']
#  json['forecast']['forecastday'][0-7]['day']['daily_chance_of_snow']
#  json['forecast']['forecastday'][0-7]['day']['avgvis_km']
#  json['forecast']['forecastday'][0-7]['day']['avghumidity']
#  json['forecast']['forecastday'][0-7]['day']['uv']
#  json['forecast']['forecastday'][0-7]['day']['condition']['text']
#
#  json['forecast']['forecastday'][0-7]['astro']['sunrise']
#  json['forecast']['forecastday'][0-7]['astro']['sunset']
#  json['forecast']['forecastday'][0-7]['astro']['moonrise']
#  json['forecast']['forecastday'][0-7]['astro']['moonset']
#  json['forecast']['forecastday'][0-7]['astro']['moon_phase']
#
#  ------------------------ hourly forecast weather data -----------------------
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['temp_c']
#         dict      list of dict   day   list   hour
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['wind_kph']
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['pressure_mb']
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['chance_of_rain']
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['chance_of_snow']
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['precip_mm']
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['humidity']
#  json['forecast']['forecastday'][0-7]['hour'][0-23]['uv']
