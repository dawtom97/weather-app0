import requests
from datetime import datetime
from config import AppConfig
from common.functions import to_celsius

API_KEY = AppConfig.API_KEY
API_CITY = AppConfig.API_CITY

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        weather = {
                "miejsce": data.get("name"),
                "temperatura": to_celsius( data.get("main").get("temp") ),
                "temperatura_odczuwalna": to_celsius(data.get("main").get("feels_like")),
                "predkosc_wiatru": data.get("wind").get("speed"),
                "cisnienie": data.get("main").get("pressure"),
                "wilgotnosc": data.get("main").get("humidity"),
                "zachmurzenie": data.get("clouds").get("all"),
                "godzina_pobrania_danych": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather
    except Exception as e:
        print("Error", e)

