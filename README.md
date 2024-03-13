**Основные задачи:**

- [/api/v1/shifts/add_shift_task] Эндпойнт добавления сменных заданий
- [/api/v1/shifts/get_task] Эндпойнт получения сменного задания по ID
- [/api/v1/shifts/update_task] Эндпойнт изменения сменного задания по ID
- [/api/v1/shifts/] Эндпойнт получения списка сменных заданий по фильтрам
- [/api/v1/shifts/aggregate] Эндпойнт "аггрегации" продукции

**Задачи "со звездочкой":**

- [Выполнено] docker

## Запуск проекта
- Первым делом нужно выполнить комманду `docker-compose up --build` для поднятия контейнеров.
- С помощью комманды `docker-compose exec fastapi sh` зайти на образ и выполнить комманды:
  Выполнить миграции через `alembic` чтобы подготовить модели для PostgreSQL - `alembic revision --autogenerate -m "Database creation"`
  Выполнить комманду для добавления моделей в базу данных - `alembic upgrade hash`(Вместо 'hash' подставить хэшированный id миграции)

Теперь вы можете перейти в документацию FastAPI и `http://host:8000/docs`(где 'host' это ip-адрес хoста на котором поднимается `docker-compose` и отправить запросы.
