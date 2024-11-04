import streamlit as st
import importlib

# Функция для загрузки пунктов меню из файла
def load_menu_items(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# Функция для загрузки надписей из текстового файла
def load_labels(file_path):
    labels = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                labels[key.strip()] = value.strip()
    return labels

# Загрузка пунктов меню и надписей
menu_items = load_menu_items("data/menu_items.txt")
labels = load_labels("data/labels.txt")

# Создание макета с колонками для заголовка и изображения
col1, col2 = st.columns([3, 1])

# В левой колонке — заголовок
with col1:
    st.title(labels["title"])

# В правой колонке — изображение
with col2:
    st.image("data/image.jpg", use_column_width=True)

# Отображение вступительного текста
st.write(labels["intro_text"])

# Выпадающее меню
selected_item = st.selectbox(labels["menu_label"], menu_items)

# Отображение сообщения о выборе
st.write(labels["selection_message"].format(item=selected_item))

# Динамическое импортирование и вызов функции
module_name = f"punkti.item{menu_items.index(selected_item) + 1}"
module = importlib.import_module(module_name)
module.show_chart()

# Отображение нижнего текста
st.write("---")  # Разделительная линия
st.write(labels["footer_text"])

