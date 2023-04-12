# Weather-checker

## О проекте:
Проект, который обращается к API сервиса https://openweathermap.org/
и узнает данные по погоде на данный момент.

### Как запустить проект

> команды указаны для Windows

Клонировать репозиторий и далее перейти в него.

```sh
git clone git@github.com:AfonyaTriceps/get_weather.git
```

Cоздать и активировать виртуальное окружение:

```sh
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```sh
pip install -r requirements.txt
```

Выполнить миграции:

```sh
python manage.py migrate
```

Запустить проект:

```sh
python manage.py runserver
```

Создайте файл `.env` в корневой директории проекта и заполните 
переменные окружения для подключения к базе PostgreSQL в нем:
* DB_ENGINE=django.db.backends.postgresql
* DB_NAME=cities
* POSTGRES_USER=postgres
* POSTGRES_PASSWORD=postgres
* DB_HOST=127.0.0.1
* DB_PORT=5432
