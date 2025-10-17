# Минимальный блог-сервер

Этот файл описывает, как собрать, запустить, протестировать и задеплоить проект сервера блога.

## 1. Сборка и запуск локально

1. Клонируйте репозиторий:
   ```bash
   git clone <repo-url>
   cd blog-server
   ```
2. Соберите и запустите сервисы:
   ```bash
   docker build -t blog-server:latest .
   docker compose up -d
   ```
3. Доступ к API:
   ```
   http://localhost:8080
   ```

## 2. Описание API

### Получить все посты
```bash
curl -i http://localhost:8080/posts
```
**Ответ:**
```json
[
  {
    "id": 1,
    "title": "Первый пост",
    "content": "Содержимое первого поста"
  }
]
```

### Создать новый пост
```bash
curl -i -X POST http://localhost:8080/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"Новый пост","content":"Текст поста"}'
```
**Ответ:**
```json
{
  "id": 2,
  "title": "Новый пост",
  "content": "Текст поста"
}
```

## 3. Технологии
- Python 3.11
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Docker

## 4. Smoke-тест
Выполните команду, чтобы убедиться в работоспособности:
```bash
curl -s http://localhost:8080/posts | jq .
```

## 5. Настройка деплоя
CI/CD настроен в файле `.github/workflows/deploy.yml` с использованием GitHub Actions. Для деплоя необходимо задать следующие секреты репозитория:
- `SSH_PRIVATE_KEY` — приватный SSH-ключ для доступа к серверу
- `SERVER_HOST` — адрес или IP сервера
- `SERVER_PORT` — SSH-порт (обычно 22)
- `SERVER_USER` — имя пользователя для SSH
- `SSH_KNOWN_HOSTS` — запись для known_hosts (чтобы избежать подтверждений)

Также на сервере деплоя нужно создать структуру каталогов:
```
~/blog-server
  └── logs
    ├── app
    └── postgres
```

Чтобы PostgreSQL мог записывать логи в директорию `postgres` выполнить:
```bash
sudo chown -R 70:70 ~/blog-server/logs/postgres
```

Процесс деплоя:
1. GitHub Actions поднимает машину, на ней собирается Docker-образ.
2. Передача образа в `tar` файле и `docker-compose.yml` на целевой сервер по SSH.
3. Загрузка образа и выполнение `docker compose up -d` на сервере
4. При необходимости старые образы и контейнеры удаляются командой `docker system prune`.