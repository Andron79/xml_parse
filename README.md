### Xml_parse
Тестовое задание соискателю на вакансию 
Middle Разработчик Python + Django
Стек
Python 3.5+
Django 3.1+

Задача
Входные данные
xml файл https://yadi.sk/d/ACKqRRoFuHS8GA
база - предпочтительно MySQL или PostgreSQL

#### Описание задачи
Парсинг следующих атрибутов
* название корневого элемента (в случае данного xml это fcsNotificationEF)
* data/purchaseNumber
* data/docPublishDate
* data/purchaseObjectInfo
* responsibleOrg/regNum
* responsibleOrg/fullName
* lot/maxPrice

Положить данные в базу данных в одноименные поля в таблицу t_procedures. 

Для хранения корневого элемента название поля будет xml_type

Сделать справочник пользователей - таблица t_users
* id (уникально)
* имя пользователя (уникально)
В t_procedures добавить поле “Куратор” - связь с таблицей t_users.
В админке вывести 2 сущности
* t_procedures 
* t_users
Вывести все поля в списках + формы редактирования
На фронте вывести график и фильтр к нему. Предпочтительно использовать AdminLTE любой версии. Например 8. Но можно и голым фреймворком отрисовать страницу.
График
* По оси X вывести даты (поле docPublishDate)
* По оси Y вывести сумму maxPrice по всем записям БД этой даты.

То есть группировка по дате и сумма значений

Фильтр над графиком
* Селект с кураторами (только те, которые есть в записях  t_procedures)
  
* При выборе куратора в селекте, обновить график. 
  * На графике вывести только данные этого куратора
* По-умолчанию показывать данные по всем кураторам - это значение в селекте “Все”

UPD. 
  * Добавить руками еще записей 5, чтобы продемонстрировать работу графика и фильтра

### Запуск проекта:
```
1. Клонировать проект
2. Активировать виртуальное окружение
3. pip install -r requirements.txt - установить зависимости
4. docker-compose up --build поднять БД в контейнере
5. ./manage.py migrate - применить миграции
6. ./manage.py createsuperuser - установить суперпользователя
7. Перейти по ссылке http://127.0.0.1:8000/parse/ - запуск парсера для начальных данных в БД 
   (XML файлы для парсера должны лежать в папке проекта /xml_files) 
8. В админке добавить кураторов к t_procedures
```