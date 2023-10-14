# Where_to_go

Проект создан, чтобы поделиться интересными местами Москвы и дать о них некоторую информацию. Стартовый сервер создает карту, на которой отмечены места из базы данных с их описанием и фотографиями. Ссылка на рабочий сайт: [DKonst21.pythonanywhere.com](https://DKonst21.pythonanywhere.com/)

## Превью

![Where_to_go_site_preview.PNG](static%2FWhere_to_go_site_preview.PNG)

## Запуск локально

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. 
```sh
git clone https://github.com/DKonst21/where_to_go
```

Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите сервер

```sh
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Дефолтное значение - `False`.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts). Дефолтное значение - `['127.0.0.1', 'localhost', '[::1]']`

Обязательным является только SECRET_KEY.

Сайт, запущенный локально, будет доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Для входа в админку и добавления/изменения данных о локациях можно использовать адрес: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Наполнение контентом
#### Для того, чтобы наполнить контентом в ручную необходимо:
 - Открыть список имеющихся мест, по адресу [http://127.0.0.1:8000/admin/places/place/](http://127.0.0.1:8000/admin/places/place/) (понадобится залогиниться в админку)
 - Найти нужную локацию по названию через поиск над списком мест
 - Перейти на страницу редактирования
 - Для изменения порядка изображений, достаточно переместить их в списке drag and drop'ом
 - Не забыть нажать кнопку <i>"сохранить"</i>

#### Для того, чтобы наполнить контентом из уже имеющегося файла необходимо:
 - создать файл в формате *.json

<i>пример составления *.json файла:</i>
```json
{
    "title": "Название места",
    "imgs": [
        "https://ссылка_на_картинку.ком/картинка.jpg",
        "https://ссылка_на_картинку.ком/картинка.jpg",
        "https://ссылка_на_картинку.ком/картинка.jpg"
    ],
    "description_short": "Короткое описание места",
    "description_long": "<p>Длинное описание, с поддержкой тэгов</p>",
    "coordinates": {
        "lng": "37,64", - координаты в числовом формате
        "lat": "55,753676"
    }
}
```
 - выгрузить его онлайн на [Github](https://github.com)
 - ввести команду с ссылкой на файл
```commandline
python manage.py load_place http://адрес/файла.json
```

<i>Пример выполнения:</i>
```commandline
(where_to_go) PS E:\where_to_go> python manage.py load_place http://адрес/файла.json
WARNING:root:Response code: 200
WARNING:root:New Place: "Новое интересное место" has been created
WARNING:root:All images has been uploaded
```

Так же можно отменить загрузку изображений для выбранного места:
```commandline
(where_to_go) PS E:\where_to_go> python manage.py load_place http://адрес/файла.json --skip_img
WARNING:root:Response code: 200
WARNING:root:New Place: "Новое интересное место" has been created
WARNING:root:Pictures uploading has been skipped...
```

## Цели проекта
Данные взяты в рамках урока [Django - Урок 1 'Пишем Яндекс.Афишу'](https://dvmn.org/modules/django/)


Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).