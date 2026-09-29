import mysql.connector as sql
from config import AppConfig

# Funkcja tworząca połączenie z bazą danych
def get_connection():
    return sql.connect(
        host = AppConfig.DB_HOST,
        user = AppConfig.DB_USER,
        password = AppConfig.DB_PASSWORD,
        database = AppConfig.DB_NAME
    )


def create_weather_table():

    query = """
    CREATE TABLE IF NOT EXISTS records (
        id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        miejsce VARCHAR(255) NOT NULL,
        temperatura FLOAT NOT NULL,
        temperatura_odczuwalna FLOAT NOT NULL,
        predkosc_wiatru FLOAT NOT NULL,
        cisnienie INT NOT NULL,
        wilgotnosc INT NOT NULL,
        zachmurzenie INT NOT NULL,
        godzina_pobrania_danych DATETIME NOT NULL
    )
    """

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabela została utworzona lub już istnieje")
    except Exception as e:
        print(e)



def save_weather_record(data):
    query = """
        INSERT INTO records 
        (miejsce,temperatura, temperatura_odczuwalna, 
        predkosc_wiatru, cisnienie, wilgotnosc, 
        zachmurzenie, godzina_pobrania_danych)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data['miejsce'],
        data['temperatura'],
        data['temperatura_odczuwalna'],
        data['predkosc_wiatru'],
        data['cisnienie'],
        data['wilgotnosc'],
        data['zachmurzenie'],
        data['godzina_pobrania_danych']
    )

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("Informacja zapisana w MySQL")
    except Exception as e:
        print(e)


def get_weather_records():
    query = """
    SELECT miejsce,temperatura, godzina_pobrania_danych 
    FROM records ORDER BY godzina_pobrania_danych DESC
    """

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(e)
