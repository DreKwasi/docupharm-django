FROM python:3.10.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /docupharm

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /docupharm/