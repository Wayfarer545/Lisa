## Базовый образ для сборки
FROM python:3.11.1-slim

# Указание рабочей директории
WORKDIR /usr/src/app

# Запрещаем Python писать файлы .pyc на диск
ENV PYTHONDONTWRITEBYTECODE 1
# Запрещает Python буферизовать stdout и stderr
ENV PYTHONUNBUFFERED 1

# Установка зависимостей проекта
COPY ./requirements.txt .
RUN pip install update pip && pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Запускаем проект
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
CMD ["python", "main.py"]
