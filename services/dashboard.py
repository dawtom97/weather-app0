import streamlit as st
import pandas as pd
from config import AppConfig

def render():
    FILE = AppConfig.WEATHER_FILE
    df = pd.read_csv(FILE)

    # Ustawienia strony
    st.set_page_config(
        page_title="Aplikacja pogodowa",
        layout="wide",
    )

    st.title("Aplikacja pogodowa")
    st.subheader("Dane pogodowe dla Warszawy, pochodzące z OpenWeatherApi")

    # Pasek boczny z ustawieniami
    st.sidebar.header("Konfiguracja")

    rows_size = st.sidebar.slider(
        "Ilość rekordów w tabeli",
        min_value=1,
        max_value=100,
        value=10,
        step=5
    )

    extra_metric = st.sidebar.selectbox(
        "Dodatkowa metryka",
        ["cisnienie","wilgotnosc","zachmurzenie"]
    )

    st.divider()
    # Informacje o najnowszym rekordzie pogodowtm
    last_row = df.iloc[-1] # ostatni rekord

    st.subheader("Aktualna pogoda")

    cols = st.columns(4)
    with cols[0]:
        temp = last_row["temperatura"]
        cols[0].metric("Temperatura", f"{temp}")
    with cols[1]:
        feels_like = last_row["temperatura_odczuwalna"]
        cols[1].metric("Temperatura odczuwalna", f"{feels_like}")
    with cols[2]:
        wind_speed = last_row["predkosc_wiatru"]
        cols[2].metric("Prędkośc wiatru", f"{wind_speed}")
    with cols[3]:
        metric_value = last_row[extra_metric]
        cols[3].metric(f"{extra_metric.title()}", f"{metric_value}")

    st.divider()


    # Wykresy liniowe
    st.subheader("Temperatura w czasie")
    temp_chart = df.set_index(
        "godzina_pobrania_danych"
    )[["temperatura","temperatura_odczuwalna"]]
    print(temp_chart)
    st.line_chart(temp_chart)

    # Wilgotność
    humidity_chart = df.set_index(
        "godzina_pobrania_danych"
    )[["wilgotnosc"]]

    st.line_chart(humidity_chart)



    st.divider()
    # Tabela z rekordami
    st.subheader(f"Najnowsze pomiary ({rows_size})")
    st.dataframe(df.tail(rows_size))




