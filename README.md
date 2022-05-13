
Написать форму доставки товара, которая должная состоять из полей:

название товара

тип товара

дата доставки

файл(аттачмент)

множественных адресов пунктов выдачи

Все должно быть написано на class BasedViews
Реализовать возможность множественного добавления адресов пунктов выдачи на формсетах с использованием данной библиотеки https://github.com/elo80ka/django-dynamic-formset
Не использовать Vue и django rest, то есть все должно быть написано на чистой django

# Запуск приложения

## Через докер

склонировать репозиторий `git clone https://github.com/TaPPa45/Nextner_form.git`

в папке с проектом в консоль `docker-compose build` затем `docker-compose up`

## Без докера

python 3.10.4

склонировать репозиторий `git clone https://github.com/TaPPa45/Nextner_form.git`

Установить зависимости `pip install -r requirements.txt`

Создать `python manage.py makemigrations` и применить `python manage.py migrate`

Собрать статику `python manage.py collectstatic`

запустить сервер `python manage.py runserver`

http://localhost:8000/create-form/
