#Dockerfile
# Usa la imagen oficial de Python 3.8
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias necesarias
RUN pip install --no-cache-dir Flask==2.0.1 Werkzeug==2.2.2


# Copia el contenido actual al contenedor en /app
COPY . /app

# Expone el puerto 5000
EXPOSE 5000

# Ejecuta server.py cuando se inicia el contenedor
CMD ["python", "server.py"]
