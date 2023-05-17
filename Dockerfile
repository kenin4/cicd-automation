# --- Build Stage ---
FROM python:3.9-slim as build

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 5000

# Run the application
CMD [ "python", "./app.py" ]
