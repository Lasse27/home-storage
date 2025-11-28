## Stage 1: Vue Build
FROM node:20-slim AS vue-build
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build


## Stage 2: Flask App
FROM python:3.12-slim AS flask-app
WORKDIR /flask-app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./
COPY --from=vue-build /app/dist ./app/static

## Pseudo Stage 3: Run app
EXPOSE 5000
CMD ["python", "run.py"]