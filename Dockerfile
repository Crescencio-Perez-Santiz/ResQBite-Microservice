# Dockerfile
FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt
RUN pip install requirements

COPY . .

EXPOSE 4242

CMD ["python", "app.py"]
