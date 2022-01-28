FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY /data .
COPY /data/file.ics ./data/file.ics

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]


