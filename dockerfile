# Base image
FROM --platform=linux/arm python:3.12-slim

# Set work directory
WORKDIR /initScripts

# Copy requirements.txt
# COPY requirements.txt .

# Install dependencies
RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get -y install curl gpg
RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
RUN apt-get update
RUN apt-get install -y nvidia-container-toolkit
RUN apt-get install nvidia-container-runtime
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install tensorrt ultralytics numpy pandas

# Copy application code
COPY initScripts/ .
COPY runs/classify/train6/ .

# Expose port
EXPOSE 8000

# Define command to run the application
CMD ["uvicorn", "main:imgPredictionApp", "--host", "127.0.0.1", "--port", "8000"]