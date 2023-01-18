FROM python:3.10-alpine
WORKDIR /client
RUN apk add --no-cache make
RUN apk add --no-cache poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install || true
COPY ./api ./api
COPY ./migration ./migrations
COPY ./.env ./.env
COPY ./Makefile ./Makefile
CMD make run