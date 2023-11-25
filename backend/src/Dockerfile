FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install werkzeug==2.0.2

COPY app.py .
COPY models.py .
COPY dataset.xlsx .

EXPOSE 5000

CMD ["python", "./app.py"]