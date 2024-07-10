FROM python:3.9-slim
# ----------------------------------------
# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg \
        lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Install NVIDIA CUDA
RUN curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub | apt-key add - && \
    echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64 /" > /etc/apt/sources.list.d/cuda.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        cuda-cudart-11-4 \
        cuda-compat-11-4 \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

# Install additional dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libcudnn8=8.2.4.15-1+cuda11.4 \
        libcudnn8-dev=8.2.4.15-1+cuda11.4 \
    && rm -rf /var/lib/apt/lists/*

# Install PyCUDA
RUN pip install numpy==1.22.0  # Adjust NumPy version as needed
RUN pip install pycuda
# ----------------------------------------
WORKDIR /
COPY . /

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]