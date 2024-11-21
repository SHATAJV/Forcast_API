import requests

API_KEY = "a678259620c3934dfe35214c28802c2a"
CITY_1 = "Toulouse"
CITY_2 = "Saint-Geours-de-Maremne"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    