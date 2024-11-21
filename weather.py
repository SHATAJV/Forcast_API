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