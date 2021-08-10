FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN python -m pip install --upgrade pip
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ..