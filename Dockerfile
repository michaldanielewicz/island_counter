FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add bash
WORKDIR /home/app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install -n --no-ansi \
COPY . .