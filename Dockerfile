FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /home/app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install -n --no-ansi
COPY . .
ENTRYPOINT ["python", "main.py"]