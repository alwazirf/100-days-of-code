import requests
api_key = "dummy"
city = "London"
latitude = 18.643061
longtitude = -91.830490
URI = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": latitude,
    "lon": longtitude,
    "appid": api_key,
    "cnt": 4
}

req = requests.get(URI, params=parameters)
req.raise_for_status()
all_data = req.json()
weather_id = all_data["weather"][0]["id"]
will_rain = False
print(all_data["weather"][0])
if weather_id < 700:
    will_rain = True
    
if will_rain:
    print("Bring an umrella")