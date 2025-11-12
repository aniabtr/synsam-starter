FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy project definition
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the app
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run app
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
