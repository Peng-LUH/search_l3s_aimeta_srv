FROM python:3.9.17-slim

WORKDIR /code
COPY . /code

# RUN apt-get update
# RUN apt-get install -y default-jre
# RUN apt-get install -y default-jdk
# RUN java --version

RUN apt-get update
RUN apt-get -y install python3-dev
RUN pip install --upgrade pip setuptools wheel pybind11
RUN pip install -e .[dev]
RUN pip install -r requirements.txt

# RUN pip install --upgrade pip setuptools wheel
# RUN python -m pip install python-dev-tools --user --upgrade
# RUN conda install -c conda-forge hdbscan
# RUN pip install --no-binary :all: faiss-cpu
# RUN pip install -e .


# RUN python initializer.py

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1
ENV FLASK_ENV="development"
ENV FLASK_RUN_PORT=5000

CMD [ "flask", "run", "--host=0.0.0.0"]

