
#Image base
FROM python:3.11-alpine

# App directory
WORKDIR /app

# Copia el archivo de requisitos y el script al contenedor
COPY requirements.txt ./
COPY NetworkMonitor.py ./

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el script para verificar las dependencias
CMD ["python", "NetworkMonitor.py"]
