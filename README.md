# Book Application

## Запуск

1. Создайте и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
    ```

    - Для Linux: `source venv/bin/activate`
    - Для Windows: `venv\Scripts\activate.bat`

2. Создайте файл `.env` с переменными, нужные переменные указаны в файле .env_example

3. Запуск приложения:

   При запуске через docker-compose впишите значения недостающих переменных в .env_docker

   ```bash
    docker compose up --build
    ```

    URL для просмотра: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    ИЛИ

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3.manage.py migrate
    python3.manage.py initadmin
   ```
   Запустите redis

   ```
   redis-server
   ```
   Запустите сервер
   ```
    python3 manage.py runserver
    ```
   Запустите celery и celery-beat

   ```
    celery -A config.celery worker -B -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
   ```
   
   
