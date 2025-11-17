## Stage 1: Vue Build
FROM node:22 AS vue-build
WORKDIR /app
COPY HomeStorage.UI/package*.json ./
RUN npm install
COPY HomeStorage.UI/ ./
RUN npm run build


## Stage 2: Flask App
FROM python:3.12-slim AS flask-app
WORKDIR /flask-app
COPY HomeStorage.Server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY HomeStorage.Server/ ./
COPY --from=vue-build /app/dist ./app/static

## Pseudo Stage 3: Run app
EXPOSE 5000
CMD ["python", "run.py"]