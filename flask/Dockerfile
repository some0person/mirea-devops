FROM python:3-alpine

RUN mkdir -p /usr/src/flask
WORKDIR /usr/src/flask

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir psycopg2-binary Flask

COPY . .

CMD ["python3", "app.py"]