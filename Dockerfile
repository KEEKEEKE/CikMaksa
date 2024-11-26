# Используем базовый образ с Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
#RUN pip install --no-cache-dir streamlit pandas matplotlib altair
# RUN pip install -r requirements.txt

# Копируем приложение и все необходимые папки внутрь контейнера
COPY app.py .
COPY requirements.txt requirements.txt
COPY data/ data/
COPY punkti/ punkti/
RUN pip install -r requirements.txt

# Указываем команду для запуска Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]

