import pandas as pd
import streamlit as st

def show_chart():
    # Загрузка данных из CSV
    df = pd.read_csv("data/item1.csv")

    # Проверка, что данные содержат нужные колонки
    if "Year" in df.columns and "Total budget" in df.columns and "Budget deficit" in df.columns:
        st.subheader("Budžets pa gadiem un tā deficīts")
        st.write("Grafikā parādīts kopējais budžets pa gadiem un cik liela daļa no tā ir deficīts.")

        # Устанавливаем "Year" как индекс для удобства построения графика
        df.set_index("Year", inplace=True)

        # Строим график с областями
        st.area_chart(df[["Total budget", "Budget deficit"]])
    else:
        st.write("Файл данных должен содержать колонки 'Year', 'Total budget' и 'Budget deficit'.")

