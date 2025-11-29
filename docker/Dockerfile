FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir flask gunicorn

COPY src/ /app/

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "example_app:app"]
