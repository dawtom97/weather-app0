import pandas as pd
from config import AppConfig
import os

def create_excel(data):
    new_df = pd.DataFrame(data)
    try:
        if os.path.exists(AppConfig.WEATHER_FILE):
            old_df = pd.read_excel(AppConfig.WEATHER_FILE)
            df = pd.concat([old_df, new_df])
            df.to_excel(AppConfig.WEATHER_FILE, index=False)
        else:
            new_df.to_excel(AppConfig.WEATHER_FILE, index=False)

    except Exception as e:
        print(e)



def read_file():
    try:
        if os.path.exists(AppConfig.WEATHER_FILE):
            df = pd.read_excel(AppConfig.WEATHER_FILE)
            return df
    except Exception as e:
        print(e)


