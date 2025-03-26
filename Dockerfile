FROM python:3.9-slim

WORKDIR /app
COPY contatore.py .

RUN pip install flask

EXPOSE 80
CMD ["python", "contatore.py"]