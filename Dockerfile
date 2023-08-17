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
RUN pip install -r requirements.txt
RUN pip install -e .[dev]

# RUN pip install --upgrade pip setuptools wheel
# RUN python -m pip install python-dev-tools --user --upgrade
# RUN conda install -c conda-forge hdbscan
# RUN pip install --no-binary :all: faiss-cpu
# RUN pip install -e .


# RUN python initializer.py

EXPOSE 5000

ENV FLASK_APP=run.py
CMD [ "flask", "run", "--host=0.0.0.0 --port=5000"]

