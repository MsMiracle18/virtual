# офіційний образ Python як базовий
FROM python:3.8

# Встановила робочу директорію всередині контейнера
WORKDIR /app

# Скопіювала файл requirements.txt в контейнер
COPY requirements.txt /app/

# Встановила залежності проекту
RUN pip install --no-cache-dir -r requirements.txt

# Скопіювала весь проект в контейнер
COPY . /app/

# Визначила точку входу для контейнера
CMD ["python", "ваш_файл_скрипту.py"]  # Замініть 'ваш_файл_скрипту.py' на назву вашого основного файлу Python.
