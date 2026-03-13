# Use Python slim base image for production
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main script
COPY main.py .

# Run the application
CMD ["python", "main.py"]