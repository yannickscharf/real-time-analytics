FROM python:latest

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the scripts and data in the container
COPY ./scripts /app/scripts
COPY ./data /app/data

# Start command
ENTRYPOINT ["python", "scripts/main.py"]