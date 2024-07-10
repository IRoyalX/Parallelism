FROM python:3.9-slim
# ----------------------------------------
FROM nvidia/cuda:11.4.1-devel-ubuntu20.04

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        build-essential \
        cuda-command-line-tools-11-4 \
        cuda-libraries-dev-11-4 \
        libcudnn8=8.2.4.15-1+cuda11.4 \
        libcudnn8-dev=8.2.4.15-1+cuda11.4

RUN pip3 install pycuda, numpy
# ----------------------------------------
WORKDIR /
COPY . /

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]