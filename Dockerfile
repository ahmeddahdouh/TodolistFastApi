FROM python:3.12-slim

WORKDIR /work

COPY pyproject.toml .
RUN pip install poetry
RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

