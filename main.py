from services.openweather_api import get_weather
from services.files import create_excel, read_file
from services.dashboard import render
from services.mysql_db import create_weather_table, save_weather_record, get_weather_records
import time

# data = read_file()
# print(data)

create_weather_table()

x = get_weather_records()
print(x)

while True:
    # #1. Pobranie danych pogodowych
    weather = get_weather()
    # #2. Wrzucenie danych do serwisu files - funkcji create_excel
    # # [weather] w liście bo pandas do DF oczekuje listy
    # create_excel([weather])
    # save_weather_record(weather)
    # print("Pobieram dane pogodowe")
    #
    time.sleep(15)

# placeholder: threads

# if "__main__" == __name__:
#     render()



