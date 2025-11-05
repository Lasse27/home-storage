# Base image
FROM python:3.12-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Dependencies kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY . .

# Port freigeben
EXPOSE 8000

CMD ["python", "run.py"]