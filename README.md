# paprika

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

Запустите базу данных и сайт:

```bash
docker-compose up
```

В новом терминале не выключая сайт запустите команды для настройки базы данных:

```bash
docker-compose run app ./manage.py migrate
docker-compose run app ./manage.py createsuperuser
```

## Пересоздаем базу

В текущих настройках (с пользователем postgres в БД) сходу не разобрался как удалить и создать заново базу `postgres`, поэтому удаляем таблицы по одной. **TODO:** запускать БД с кастомным пользователем и базой.

Подключаемся к контейнеру с базой:

```bash
docker exec -it paprika-db-1 psql -U postgres
```

Несколько раз выполнить команду:

```sql
drop table table_name cascade;
```
