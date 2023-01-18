include .env
export

ALEMBIC = database

migrate:
	cd ${ALEMBIC} && poetry run alembic upgrade head

revision:
	cd ${ALEMBIC} && poetry run alembic revision --autogenerate

upgrade:
	cd ${ALEMBIC} && poetry run alembic upgrade +1

downgrade:
	cd ${ALEMBIC} && poetry run alembic downgrade -1

shell:
	poetry shell

logs:
	docker-compose logs

postgres:
	docker-compose up -d postgresql

down:
	docker-compose down

build:
	docker-compose build --no-cache

migrator:
	docker-compose up migrator

open_postgres:
	PGPASSWORD=${DB_PASSWORD} psql -U ${DB_USERNAME} -d ${DB_NAME}
