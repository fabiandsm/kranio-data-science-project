FROM python:3.11-slim

# Carpeta dentro del contenedor
WORKDIR /app

# Copiamos dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el proyecto
COPY . .

# Exponemos puerto
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]


