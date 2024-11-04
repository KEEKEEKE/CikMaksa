import pandas as pd
import streamlit as st

def show_chart():
    # Загружаем данные из CSV
    df = pd.read_csv("data/item3.csv")

    # Проверка структуры данных
    if "Категория" in df.columns and "Сумма" in df.columns:
        # Строим круговую диаграмму
        st.subheader("Budžeta struktūra")
        st.write("Budžeta sadalījuma sektoru diagramma pa kategorijām:")

        # Построение диаграммы
        st.pyplot(df.set_index("Категория").plot.pie(y="Сумма", legend=False, autopct='%1.1f%%').get_figure())
    else:
        st.write("Файл данных должен содержать колонки 'Категория' и 'Сумма'.")

