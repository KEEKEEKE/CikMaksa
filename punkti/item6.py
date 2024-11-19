import streamlit as st

def show_chart():
    # Создаем две колонки
    col1, col2 = st.columns([1, 1])

    # В первой колонке — изображение на половину ширины страницы
    with col1:
        st.image("data/item6.png", use_container_width=True)

    # Во второй колонке — текст из файла item6.txt
    with col2:
        with open("data/item6.txt", "r", encoding="utf-8") as file:
            text_content = file.read()
        st.write(text_content)

