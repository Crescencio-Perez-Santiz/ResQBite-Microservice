FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY fullchain.pem privkey.pem /app/

COPY . .

EXPOSE 5003

CMD ["python", "UserMain.py"]