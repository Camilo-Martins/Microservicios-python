FROM python:3.10-slim

WORKDIR /app

# Dependencias necesarias para mysqlclient + mysqladmin
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    default-mysql-client \
    netcat-openbsd \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copiar proyecto
COPY . .

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]