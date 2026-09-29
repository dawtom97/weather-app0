import dotenv
import os
dotenv.load_dotenv()

class AppConfig:
    API_KEY = os.getenv("API_KEY")
    API_CITY = os.getenv("API_CITY")
    WEATHER_FILE = "weather.xlsx"
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

