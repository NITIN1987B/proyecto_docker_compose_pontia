#  Crear Dockerfile para la aplicación FastAPI


FROM python:3.11-slim

# Crea el usuario appuser, su carpeta personal y le asigna el UID 1000
RUN useradd -m -u 1000 appuser    

# Establecer directorio de trabajo
WORKDIR /app                       


# copiamos el archivo dependencias
COPY requirements.txt .
#Instala dependencias python
RUN pip install --no-cache-dir -r requirements.txt

#  Copia el proyecto dentro de /app
COPY . .

# da al usuario appuser la propiedad de los archivos de /app
RUN chown -R appuser:appuser /app

# activamos appuser para las siguientes instrucciones
USER appuser

#  informa de que fastApi escucha en el puerto 8080
EXPOSE 8080

# arranca la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
