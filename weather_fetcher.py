import requests

from datetime import datetime

API_KEY = "46e72ff86a97c6f01921a6a9427cd553"

CITY = "Chennai"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather():

    params = {

        "q": CITY,

        "appid": API_KEY,

        "units": "metric"

    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    weather = {

        "date": datetime.now().strftime("%Y-%m-%d"),

        "temperature": data["main"]["temp"],

        "humidity": data["main"]["humidity"]

    }

    return weather

# import requests

# from datetime import datetime

# API_KEY = "YOUR_API_KEY"

# CITY = "Chennai"

# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# def fetch_weather():

#     params = {

#         "q": CITY,

#         "appid": API_KEY,

#         "units": "metric"

#     }

#     response = requests.get(BASE_URL, params=params)

#     data = response.json()

#     weather = {

#         "date": datetime.now().strftime("%Y-%m-%d"),

#         "temperature": data["main"]["temp"],

#         "humidity": data["main"]["humidity"]

#     }

#     return weather
 