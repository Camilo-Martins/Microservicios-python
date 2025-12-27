FROM python:3.10-slim

WORKDIR /app

# Dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-mysql-client \
    gcc \
    pkg-config \
    default-libmysqlclient-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
