from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List
import logging

# TODO: Configurar logging
# logging.basicConfig(...)

# TODO: Configurar conexión a base de datos
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

app = FastAPI(title="CRUD API", version="1.0.0")

# TODO: Definir modelos Pydantic
# class EstudianteCreate(BaseModel):
#     nombre: str
#     email: str
#     edad: int

# class EstudianteResponse(BaseModel):
#     id: int
#     nombre: str
#     email: str
#     edad: int

# TODO: Implementar endpoints CRUD
# @app.get("/estudiantes", response_model=List[EstudianteResponse])
# def listar_estudiantes():
#     """Lista todas las entidades"""
#     pass

# @app.get("/estudiantes/{estudiante_id}", response_model=EstudianteResponse)
# def obtener_estudiante(estudiante_id: int):
#     """Recupera una entidad específica"""
#     pass

# @app.post("/estudiantes", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED)
# def crear_estudiante(estudiante: EstudianteCreate):
#     """Crea una nueva entidad"""
#     pass

# @app.delete("/estudiantes/{estudiante_id}", status_code=status.HTTP_204_NO_CONTENT)
# def eliminar_estudiante(estudiante_id: int):
#     """Borra una entidad"""
#     pass

@app.get("/")
def root():
    return {"message": "CRUD API"}
