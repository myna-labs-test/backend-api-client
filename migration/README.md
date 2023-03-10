# Миграции бд
Репозиторий для осуществления миграций базы данных.
## Требования для установки
- `Make` версии 4.4 и выше
- `Python` версии 3.10 и выше
- `Poetry` версии 1.3.1 и выше
- (Опционально)`Docker` версии 20.10.22 и выше
## Подготовка к запуску
### Заполнение .env
Необходимо создать в корневой папке проекта файл `.env` с переменными окружения.
Пример заполнения:
```shell
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_NAME=myna_labs_test
DB_HOST=postgresql
```
### Установка зависимостей
Для локального запуска:
```shell
make prepare
```
Для запуска в докере:
```shell
make build
```
## Запуск
### Запуск в докере
Поднятие базы данных:
```shell
make postgres
```
Осуществление миграций:
```shell
make migrator
```
### Локальный запуск
```shell
make migrate
```