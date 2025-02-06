# WeatherAPI-with-Python
A short CLI use of weatherapi API for learning purposes
# Documention for the API
[https://www.weatherapi.com/docs/](https://www.weatherapi.com/docs/)

# Useful values in the response json
------------------------ current weather data -----------------------------/
response.json()['current']['condition']['text'] - text condition for current weather/
response.json()['current']['feelslike_c'] - feels like temp/
response.json()['current']['temp_c'] - temp/
response.json()['current']['wind_kph'] - wind speed/
response.json()['current']['wind_dir'] - wind direction/
response.json()['current']['wind_degree'] - exact wind direction/
response.json()['current']['pressure_mb'] - barometric pressure/
response.json()['current']['humidity'] - barometric pressure/
response.json()['current']['precip_mm'] - precipitation in mm/

---------------------------- location data ----------------------------------/
response.json()['location']['country']/
response.json()['location']['localtime']/
response.json()['location']['tz_id']/
response.json()['location']['name']/
response.json()['location']['region']/

------------------------ forecast weather data ------------------------------/
response.json()['forecast']['forecastday'][0-7]['date'] - date of forecast/
    dict      list of dict   day/
response.json()['forecast']['forecastday'][0-7]['day'] - forecast for the whole day/
response.json()['forecast']['forecastday'][0-7]['day']['mintemp_c']/
response.json()['forecast']['forecastday'][0-7]['day']['avgtemp_c']/
response.json()['forecast']['forecastday'][0-7]['day']['maxtemp_c']/
response.json()['forecast']['forecastday'][0-7]['day']['totalprecip_mm']/
response.json()['forecast']['forecastday'][0-7]['day']['daily_chance_of_rain']/
response.json()['forecast']['forecastday'][0-7]['day']['daily_chance_of_snow']/
response.json()['forecast']['forecastday'][0-7]['day']['avgvis_km']/
response.json()['forecast']['forecastday'][0-7]['day']['avghumidity']/
response.json()['forecast']['forecastday'][0-7]['day']['uv']/
response.json()['forecast']['forecastday'][0-7]['day']['condition']['text']/

response.json()['forecast']['forecastday'][0-7]['astro']['sunrise']/
response.json()['forecast']['forecastday'][0-7]['astro']['sunset']/
response.json()['forecast']['forecastday'][0-7]['astro']['moonrise']/
response.json()['forecast']['forecastday'][0-7]['astro']['moonset']/
response.json()['forecast']['forecastday'][0-7]['astro']['moon_phase']/

------------------------ hourly forecast weather data -----------------------/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['temp_c']/
    dict      list of dict   day   list   hour/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['wind_kph']/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['pressure_mb']/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['chance_of_rain']/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['chance_of_snow']/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['precip_mm']/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['humidity']/
response.json()['forecast']['forecastday'][0-7]['hour'][0-23]['uv']/
