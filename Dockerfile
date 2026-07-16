#  Crear Dockerfile para la aplicación FastAPI


FROM python:3.11-slim

# Crea el usuario appuser, su carpeta personal y le asigna el UID 1000
RUN useradd -m -u 1000 appuser    

# Establecer directorio de trabajo
WORKDIR /app                       

# TODO: Instalar dependencias del sistema necesarias (gcc, postgresql-client)
# RUN apt-get update && apt-get install -y ...

# copiamos el archivo dependencias
COPY requirements.txt .

#Instala dependencias python
RUN pip install --no-cache-dir -r requirements.txt

# TODO: Copiar código de la aplicación
# COPY . .

# TODO: Cambiar ownership y usuario
# RUN chown -R appuser:appuser /app
# USER appuser

# TODO: Exponer puerto 8080
# EXPOSE 8080

# TODO: Ejecutar aplicación con uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
