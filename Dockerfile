FROM python:latest

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the scripts and data in the container
COPY ./scripts /app/scripts
COPY ./data /app/data

# Start command
ENTRYPOINT ["bash"]