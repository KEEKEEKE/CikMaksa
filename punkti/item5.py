import pandas as pd
import streamlit as st

def show_chart():
    # Загрузка данных из CSV
    df = pd.read_csv("data/item5.csv")
    
    # Построение графика
    st.line_chart(df)

