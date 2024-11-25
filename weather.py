import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
city_1 = "Toulouse"
city_2 = "Saint-Geours-de-Maremne"
city_3= "Teheran"

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"


def get_weather(city):
    """
    Fetch the weather forecast for a given city from the OpenWeatherMap API.

    Args:
        city (str): The name of the city for which the weather forecast is requested.

    Returns:
        dict: The weather forecast data in JSON format if the request is successful,
              or None if the request fails.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()

    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None


forecast_toulouse = get_weather(city_1)
forecast_saint_geours_de_maremne = get_weather(city_2)
forecast_teheran = get_weather(city_3)

def temperatures(weather):
    """
    Extracts the minimum and maximum temperatures for the next 5 days from the weather data.

    Args:
        weather (dict): The weather forecast data for a city in JSON format.

    Returns:
        dict: A dictionary with the dates as keys and the corresponding minimum and maximum temperatures.
    """
    daily_forecast = {}
    today = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")

    for entry in weather["list"]:
        date = entry["dt_txt"].split(" ")[0]
        if today <= date <= end_date:
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

if forecast_saint_geours_de_maremne:
    saint_geours_temps = temperatures(forecast_saint_geours_de_maremne)
    print("\nTemperature forecast for Saint-Geours-de-Maremne:")
    for date, temps in saint_geours_temps.items():
        print(f"{date}: Min {temps['min']}°C, Max {temps['max']}°C")

if forecast_teheran:
    teheran_temps = temperatures(forecast_teheran)
    print("\nTemperature forecast for Teheran:")
    for date, temps in teheran_temps.items():
        print(f"{date}: Min {temps['min']}°C, Max {temps['max']}°C")