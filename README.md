# API для социальной сети Yatube

## Описание проекта

API для социальной сети Yatube предоставляет программный интерфейс для взаимодействия с платформой. API позволяет создавать публикации, комментарии, управлять подписками и работать с сообществами. Аутентификация осуществляется с помощью JWT-токенов.

## Технологии

- Python
- Django
- Django REST Framework
- Simple JWT
- PyJWT
- Pillow
- Pytest
- Requests

## Установка и запуск

### Клонирование репозитория

git clone https://github.com/IvanTishk0/api_final_yatube.git
cd api_final_yatube

### Создание и активация виртуального окружения

python -m venv env
source env/bin/activate  # для Linux и macOS
env\Scripts\activate  # для Windows

### Установка зависимостей

pip install -r requirements.txt

### Выполнение миграций

cd yatube_api
python manage.py migrate

### Запуск сервера

python manage.py runserver

### Запуск тестов

pytest

## Документация API

После запуска сервера документация API будет доступна по адресу: http://127.0.0.1:8000/redoc/

## Примеры использования API

### Получение JWT-токена

curl -X POST http://127.0.0.1:8000/api/v1/jwt/create/ -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}'

### Получение списка публикаций

curl -X GET http://127.0.0.1:8000/api/v1/posts/ -H "Authorization: Bearer <your_token>"

### Создание новой публикации

curl -X POST http://127.0.0.1:8000/api/v1/posts/ -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" -d '{"text": "Текст публикации", "group": null}'

### Получение комментариев к публикации

curl -X GET http://127.0.0.1:8000/api/v1/posts/1/comments/ -H "Authorization: Bearer <your_token>"

### Добавление комментария к публикации

curl -X POST http://127.0.0.1:8000/api/v1/posts/1/comments/ -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" -d '{"text": "Текст комментария"}'

### Получение списка сообществ

curl -X GET http://127.0.0.1:8000/api/v1/groups/ -H "Authorization: Bearer <your_token>"

### Подписка на пользователя

curl -X POST http://127.0.0.1:8000/api/v1/follow/ -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" -d '{"following": "username_to_follow"}'

## Доступные эндпоинты

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| POST | `/api/v1/jwt/create/` | Получение JWT-токена |
| POST | `/api/v1/jwt/refresh/` | Обновление JWT-токена |
| POST | `/api/v1/jwt/verify/` | Проверка JWT-токена |
| GET | `/api/v1/posts/` | Получение списка публикаций |
| POST | `/api/v1/posts/` | Создание публикации |
| GET | `/api/v1/posts/{id}/` | Получение публикации по id |
| PUT | `/api/v1/posts/{id}/` | Обновление публикации по id |
| PATCH | `/api/v1/posts/{id}/` | Частичное обновление публикации по id |
| DELETE | `/api/v1/posts/{id}/` | Удаление публикации по id |
| GET | `/api/v1/posts/{post_id}/comments/` | Получение комментариев к публикации |
| POST | `/api/v1/posts/{post_id}/comments/` | Добавление комментария к публикации |
| GET | `/api/v1/posts/{post_id}/comments/{id}/` | Получение комментария по id |
| PUT | `/api/v1/posts/{post_id}/comments/{id}/` | Обновление комментария по id |
| PATCH | `/api/v1/posts/{post_id}/comments/{id}/` | Частичное обновление комментария по id |
| DELETE | `/api/v1/posts/{post_id}/comments/{id}/` | Удаление комментария по id |
| GET | `/api/v1/groups/` | Получение списка сообществ |
| GET | `/api/v1/groups/{id}/` | Получение информации о сообществе |
| GET | `/api/v1/follow/` | Получение подписок пользователя |
| POST | `/api/v1/follow/` | Подписка на пользователя |

## Параметры запросов

### Пагинация

Для эндпоинтов, возвращающих списки объектов, доступна пагинация с параметрами:
- `limit` — количество объектов на страницу
- `offset` — номер страницы, с которой начинать выдачу

Пример: `/api/v1/posts/?limit=10&offset=0`

### Поиск

Для эндпоинта `/api/v1/follow/` доступен поиск по имени пользователя с параметром:
- `search` — строка для поиска

Пример: `/api/v1/follow/?search=username`

## Требования к версиям

Проект разработан и протестирован с использованием следующих версий пакетов:
Django==3.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0

## Авторы

- Иван Тишко
