import pandas as pd
import streamlit as st

def show_chart():
    # Загружаем данные из CSV
    df = pd.read_csv("data/item3.csv")

    # Проверка структуры данных
    if "Kat" in df.columns and "Summa" in df.columns:
        # Строим круговую диаграмму
        st.subheader("Budžeta struktūra")
        st.write("Budžeta sadalījuma sektoru diagramma pa kategorijām:")

        # Построение диаграммы
        st.pyplot(df.set_index("Kat").plot.pie(y="Summa", legend=False, autopct='%1.1f%%').get_figure())
    else:
        st.write("Файл данных должен содержать колонки 'Kategorija Summa'.")

