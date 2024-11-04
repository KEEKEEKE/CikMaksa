import pandas as pd
import streamlit as st
import altair as alt

def show_chart():
    # Загрузка данных из CSV
    df = pd.read_csv("data/item2.csv")

    # Проверка, что данные содержат нужные колонки
    if "Год" in df.columns and "Госдолг" in df.columns and "Население" in df.columns:
        # Вычисляем долг на каждого жителя и добавляем как новый столбец
        df["Долг на жителя"] = df["Госдолг"] / df["Население"]

        # Построение линейного графика с использованием Altair для отображения подсказок
        st.subheader("Valsts parāds pa gadiem")
        st.write("Līniju diagramma, kurā parādīts valsts parāds pa gadiem, ar informāciju par parādu uz vienu iedzīvotāju.")

        line_chart = alt.Chart(df).mark_line(point=True).encode(
            x="Год:O",
            y="Госдолг:Q",
            tooltip=["Год", "Госдолг", alt.Tooltip("Долг на жителя:Q", format=".2f")]
        ).properties(
            width=700,
            height=400
        )

        # Отображаем график
        st.altair_chart(line_chart, use_container_width=True)
    else:
        st.write("Файл данных должен содержать колонки 'Год', 'Госдолг' и 'Население'.")

