FROM python:3-alpine

RUN mkdir -p /usr/src/django
WORKDIR /usr/src/django

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir psycopg2-binary Django

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
