# Dockerfile
FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt requirements.txt
# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 4242

CMD ["python", "app.py"]
