# Yatube

## Описание

**Yatube** - проект социальной сети, в которой можно 
публиковать записи, комментировать их и подписываться 
на других авторов

## Установка и запуск проекта

Клонировать репозиторий и перейти в него в командной строке
```commandline
git clone https://github.com/Nokvix/api_final_yatube.git
```
```commandline
cd api_final_yatube
```

Создать и активировать виртуальное окружение

Windows
```commandline
python -m venv venv
venv/Scripts/activate
```
Linux
```commandline
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt
```commandline
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции
```commandline
cd yatube_api
python manage.py migrate
```

Запустить проект
```commandline
python manage.py runserver
```

## Пример работы с API

### Для всех пользователей

Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

```commandline
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```

### Для авторизованных пользователей

* Создание публикации

    ```commandline
    POST /api/v1/posts/
    ```
    
    ```commandline
    {
        "text": "string",
        "image": "string",
        "group": 0
    }
    ```
* Обновление публикации

    ```commandline
    PUT /api/v1/posts/{id}/
    ```
  
    ```commandline
    {
        "text": "string",
        "image": "string",
        "group": 0
    }
    ```
  
* Удаление публикации

    ```commandline
    DELETE /api/v1/posts/{id}/
    ```
  
* Получение доступа к эндпоинту ```/api/v1/follow/``` 
(подписки) доступен только для авторизованных пользователей

    Подписки пользователя от имени которого сделан запрос
  
    ```commandline
    GET /api/v1/follow/
    ```
  
* Добавлять сообщества в проект можно только через админ панель Django

* Доступ авторизованным пользователем доступен по JWT-токену (Joser), 
который можно получить выполнив POST запрос по адресу:

    ```commandline
    POST /api/v1/jwt/create/
    ```
  
    ```commandline
    {
        "username": "string",
        "password": "string"
    }
    ```
  
* Обновить JWT-токен:

    ```commandline
    POST /api/v1/jwt/refresh/
    ```
  
* пагинация (LimitOffsetPagination)

  ```commandline
  GET /api/v1/posts/?limit=5&offset=0
  ```
