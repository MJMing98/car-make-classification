# Base image
FROM python:3.12-slim

# Set work directory
WORKDIR /initScripts

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Define command to run the application
CMD ["uvicorn", "main:imgPredictionApp", "--host", "127.0.0.1", "--port", "8000"]