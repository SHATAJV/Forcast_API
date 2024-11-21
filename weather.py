import requests

API_KEY = "a678259620c3934dfe35214c28802c2a"
city_1 = "Toulouse"
city_2 = "Saint-Geours-de-Maremne"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"error to get {city}: {response.status_code}")
        return None


forecast_toulouse = get_weather(city_1)
forecast_saint_geours = get_weather(city_2)


def temperatures(weather):
    daily_forecast = {}
    for entry in weather["list"]:
        date = entry["dt_txt"].split(" ")[0]
        temp_min = entry["main"]["temp_min"]
        temp_max = entry["main"]["temp_max"]

        if date not in daily_forecast:
            daily_forecast[date] = {"min": temp_min, "max": temp_max}
        else:
            daily_forecast[date]["min"] = min(daily_forecast[date]["min"], temp_min)
            daily_forecast[date]["max"] = max(daily_forecast[date]["max"], temp_max)
        return daily_forecast


if forecast_toulouse:
    toulouse_temps = temperatures(forecast_toulouse)
    print("Temperature forecast for Toulouse:")
    for date, temps in toulouse_temps.items():
        print(f"{date}: Min {temps['min']}°C, Max {temps['max']}°C")


if forecast_saint_geours:
    saint_geours_temps = temperatures(forecast_saint_geours)
    print("Temperature forecast for Saint-Geours-de-Maremne:")
    for date, temps in saint_geours_temps.items():
        print(f"{date}: Min {temps['min']}°C, Max {temps['max']}°C")