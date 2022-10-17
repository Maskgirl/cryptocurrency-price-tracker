# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /cryptocurrency_price_tracker
COPY requirements.txt /cryptocurrency_price_tracker/
RUN pip install -r requirements.txt
COPY . /cryptocurrency_price_tracker/