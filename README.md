# Проект `YaCut` для создания коротких версий ссылок. Вводите вашу ссылку, в ответ получаете её укороченную версию.

## Стек:
* python
* Alembic
* SQLAlchemy
* WTForms
* Flask-Migrate
* Flask-SQLAlchemy
* Flask-WTF
* Jinja2

### Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone 
```

```sh
cd yacut
```

### Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```sh
    source venv/bin/activate
    ```

* Если у вас windows

    ```sh
    source venv/scripts/activate
    ```

### Установить зависимости из файла requirements.txt:

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

### Создать репозиторий для БД и файлы миграции:

```sh
flask db init
```

```sh
flask db migrate -m "<any comments>"
```

### Применить миграции:

```sh
flask db upgrade
```

### Запустить проект локально:

```sh
flask run
```

## Api:

### `POST`-запрос на создание новой короткой ссылки: `/api/id/`
```json
{
    "url": "string",
    "custom_id": "string"
}
```

### `GET`-запрос на получение оригинальной ссылки по указанному короткому идентификатору. `/api/id/<short_id>/`

Автор [GitHub - dmitryavdeevkrsk](https://github.com/avdeevdmitrykrsk/)