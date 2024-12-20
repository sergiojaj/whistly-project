# Use a lightweight base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy dependency files first
COPY pyproject.toml poetry.lock /code/

# Install Python dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy the application code
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Default entrypoint to handle migrations and then run the server
ENTRYPOINT ["sh", "-c", "poetry run python manage.py makemigrations && poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000"]

## Reminders:
# docker network create whistly-network
# docker pull postgres:latest
# docker build -t whistly-app .
# docker run  -d --name postgres-container --network whistly-network -e POSTGRES_DB=whistly -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres postgres:latest && echo "sleeping 10 seconds" && sleep 10s && docker run --name whistly-app --network whistly-network -p 8000:8000 --env-file .env -d whistly-app && echo "sleeping 10 seconds" && sleep 10s && echo "Done"