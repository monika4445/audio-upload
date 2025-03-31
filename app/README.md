# Сервис загрузки аудиофайлов

Этот проект представляет собой сервис для загрузки аудиофайлов с использованием FastAPI, SQLAlchemy и Docker. Пользователи могут загружать аудиофайлы, указывать имена файлов через API и авторизоваться через Яндекс OAuth. Файлы хранятся локально, без использования облачного хранилища.

## Функциональность

- Авторизация пользователей через Яндекс OAuth
- Загрузка аудиофайлов
- Хранение информации о файлах в базе данных PostgreSQL 16
- Использование асинхронного кода

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/NarekAvetisyan2/Projects-with-Python/tree/main/Audio_Upload_Service
cd audio-upload-service
```

### 2. Настройка окружения

Создайте `.env` файл и укажите в нем:

```env
DATABASE_URL=postgresql+asyncpg://user:password@db/audio_upload
YANDEX_CLIENT_ID=your_client_id
YANDEX_CLIENT_SECRET=your_client_secret
```

### 3. Запуск через Docker

```bash
docker-compose up --build
```

### 4. Запуск без Docker

#### Установка зависимостей

```bash
pip install -r requirements.txt
```

#### Запуск сервера

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Использование API

### 1. Авторизация

Перейдите по адресу:

```
GET /user/login
```

После успешной авторизации пользователь будет перенаправлен на `callback`.

### 2. Загрузка аудиофайла

```
POST /audio/upload
```

Тело запроса:

"""json
{
  "filename": "example.mp3",
  "file": <binary>
}
"""

### 3. Получение списка аудиофайлов пользователя

```
GET /audio/list
```

Ответ:

```json
[
  {"id": 1, "filename": "example.mp3", "filepath": "uploads/example.mp3"}
]
```

## Структура проекта

```
app/
├── databases/
│   ├── sessions.py
├── models/
│   ├── base.py
│   ├── user.py
│   ├── audio.py
├── routers/
│   ├── user.py
│   ├── audio.py
├── schemas/
│   ├── user.py
│   ├── audio.py
├── services/
│   ├── user_service.py
│   ├── audio_service.py
├── setting/
│   ├── config.py
│   ├── oauth.py
├── main.py
՛՛՛