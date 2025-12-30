# Library API

Простой проект REST API на FastAPI с базой данных SQLite.

## Установка

1. Клонируем репозиторий:

git clone https://github.com/Leo-the-developer/db-library-api.git
cd db-library-api

2. Создаем виртуальное окружение и активируем его:

python -m venv venv
venv\Scripts\activate.bat

3. Устанавливаем зависимости:

pip install -r requirements.txt

## Запуск сервера

python -m uvicorn app.main:app --reload

- Swagger UI: `http://127.0.0.1:8000/docs`

## Заполнение базы тестовыми данными

python scripts/fill_data.py

## Доступные endpoint’ы

- **/books** (GET, POST) — книги с сортировкой `sort_by=id|title|year|rating`  
- **/users** (POST) — добавление пользователя  
- **/loans** (POST) — создание выдачи  
- **/loans/with-users** (GET) — JOIN выдач с пользователями и книгами  
- **/books/category-count** (GET) — GROUP BY по категориям  
- **/books/update-rating** (PUT) — обновление рейтинга всех книг автора