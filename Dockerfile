FROM python:3.9-slim

# Installa le dipendenze di sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Crea e imposta la working directory
WORKDIR /app

# Copia i file dell'app
COPY app.py .
COPY templates ./templates

# Installa Flask
RUN pip install Flask

# Espone la porta del server
EXPOSE 80

# Comando di avvio
CMD ["python", "app.py"]