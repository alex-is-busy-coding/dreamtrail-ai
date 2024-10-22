# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set build-time argument for environment (default to production)
ARG ENVIRONMENT=production

# Copy project files into the container
COPY . .

# Install project dependencies using Poetry based on the ENVIRONMENT
RUN if [ "$ENVIRONMENT" = "development" ]; then \
    poetry install --no-root; \
    else \
    poetry install --no-root --without dev; \
    fi

# Expose FastAPI's default port
EXPOSE 8000

# Start FastAPI with Uvicorn, using a different command for development and production
CMD ["sh", "-c", "if [ \"$ENVIRONMENT\" = \"development\" ]; then poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload; else poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000; fi"]