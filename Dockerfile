# Building and running the application
FROM python:3.11-slim

WORKDIR /code

# Copy only requirements first
# If dependencies don't change - skip re-install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

WORKDIR /code/app

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
