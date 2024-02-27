FROM python:3.9-slim

WORKDIR /code
COPY . /code

RUN apt-get update
RUN apt-get -y install python3-dev
RUN pip install --upgrade pip setuptools wheel pybind11
RUN pip install -e .
RUN pip install -r requirements.txt

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=9041


CMD [ "flask", "run", "--port=9041", "--host=0.0.0.0"]

EXPOSE 9041