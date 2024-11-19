import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def show_chart():
    # Загрузка данных из CSV
    df = pd.read_csv("data/item1.csv")

    # Проверка, что данные содержат нужные колонки
    
    if "Year" in df.columns and "Total budget" in df.columns and "Budget deficit" in df.columns:
        
        st.write("Grafikā parādīts kopējais budžets pa gadiem un cik liela daļa no tā ir deficīts.")
        # Выбор данных за последний год
        last_year_data = df.loc[df["Year"] == df["Year"].max()]

        # Построение линейного графика (бюджет и дефицит по годам)
        st.subheader("Budžets pa gadiem un tā deficīts")
        fig, ax = plt.subplots()
        ax.plot(df["Year"], df["Total budget"], label="Total budget", marker="o")
        ax.plot(df["Year"], df["Budget deficit"], label="Budget deficit", marker="o", linestyle="--")
        ax.set_xlabel("Year")
        ax.set_ylabel("Сумма")
        ax.legend()
        st.pyplot(fig)




        if not last_year_data.empty:
            # Извлечение значений бюджета и дефицита
            budget = last_year_data["Total budget"].values[0]
            deficit = last_year_data["Budget deficit"].values[0]
            surplus = budget - deficit  # Рассчитываем оставшуюся часть бюджета

            
            # Построение круговой диаграммы
            st.subheader(f"Структура бюджета за {df['Year'].max()} год")
            pie_data = [surplus, deficit]
            labels = ["Оставшийся бюджет", "Дефицит"]
            fig, ax = plt.subplots()
            ax.pie(
                pie_data,
                labels=labels,
                autopct="%1.1f%%",
                startangle=90,
                colors=["#66b3ff", "#ff6666"]
            )
            ax.axis("equal")  # Круговая диаграмма в виде круга
            st.pyplot(fig)


        else:
            st.warning("Нет данных для последнего года.")

           
  
    else:
        st.write("Файл данных должен содержать колонки 'Year', 'Total budget' и 'Budget deficit'.")

