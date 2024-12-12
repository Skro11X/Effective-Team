# Effective-team test project
Проект был создан для того чтобы показать уровень умений для стажировки в компании
## Описание
Реализовано API с помощью инструмента DRF. 
Проект представляет собой CRUD для [моделей](effective_team/models.py):

1. **Команда (Team):**
    - Название команды (строка, уникальное значение).
    - Создатель команды (ссылка на модель "Создатель команды").
2. **Создатель команды (Creator):**
    - Имя (строка).
    - Деньги (баллы, float).
3. **Участник (Member):**
    - Имя (строка).
    - Выносливость (целое число).
    - Команда (ссылка на модель "Команда").
4. **Заявка в команду (TeamApplication):**
    - Участник (ссылка на модель "Участник").
    - Команда (ссылка на модель "Команда").

### Представления 

Ответы на запросы к серверу реализованны с помощью наследования от классов rest_framework.generics DRF. [Ссылка на представленя](effective_team/views)

Для модели [`TeamApplication`](effective_team/models.py) реализован класс [`TeamApplicationAPIView`](effective_team/views/team_aplication.py) с  логикой вывода списком. Список отсортирован по полю endurance и ограничен по количеству в 10 выводимых записей.

К моделям [`Creator`](effective_team/models.py), [`Team`](effective_team/models.py), [`Member`](effective_team/models.py) производится обращение к конкретному элементу с помощью указания id в адресе. Для них реализованны соответсвующие представления [`CreatorAPIView`](effective_team/views/creator.py), [`TeamAPIView`](effective_team/views/team.py), [`MemberAPIView`](effective_team/views/member.py).

Так же с помощью [RotateScoreAPIView](effective_team/views/rotate_score.py) реализована передача баллов создателя команды. Данное представление обрабатывает только `POST` запрос. Обращается к телу запроса достает из него по ключам `creator_from` и `creator_to` значения `id` двух создателей команды между которыми нужно произвести перевод. Так же ищет в теле ключ `score`, чтобы понять на какую сумму нужно сделать перевод.
Внутри производится проверка на возможность перевода

Пример запроса:
```json
{
    "creator_from": 1,
    "creator_to": 2,
    "score": 5
}
```
Пример ответа:
```json
{
    "Alex Merser": 107.0,
    "ILya Verchenko": 6.0
}
```

### Эндпоинты

| HTTP-метод                | Эндпоинт             | Описание                           |
|---------------------------|----------------------|------------------------------------|
| GET,POST,PUT/PATCH,DELETE | `/creator/<int:pk>/` | Обращение к модели Creator         | 
| GET,POST,PUT/PATCH,DELETE | `/member/<int:pk>/`  | Обращение к модели Member          | 
| GET,POST,PUT/PATCH,DELETE | `/team/<int:pk>/`    | Обращение к модели Team            | 
| GET,POST,PUT/PATCH,DELETE | `/team_application/` | Обращение к модели TeamApplication | 
| POST                      | `/rotate_score`      | Сделать перевод score              | 
| GET                       | `/shema/swagger-ui/` | Ссылка на схему к API              |
    

[Файл с эндпоинтами](effective_team/urls.py)

## Установка
1. Скачать репозиторий
```shell
    git clone https://github.com/Skro11X/Effective-Team
```
2. Установить зависимости
```shell
pip install -r requirements.txt
```
3. Установить переменные окружения из файла `.env`
4. Установить postgres и создать там базу и пользователей, значения которых указаны в `.env`
5. Либо открыть папку как проект в IDE, либо открыть папку в командной строке
6. Провести миграции 
```shell
python manage.py migrate
```
7. Запустить сервер.
```shell
python manage.py runserver
```
## Поддержка
Если будут вопросы по проекту мой тг [ilya](https://t.me/helllo_i)
