FROM python:3.9-slim
WORKDIR /
COPY . /

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

<<<<<<< HEAD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
=======
CMD ["uvicorn", "app:main"]
>>>>>>> 5abc4861b33bb2fd35d03b5b2599901781a6a775
