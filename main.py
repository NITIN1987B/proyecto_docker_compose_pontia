import logging
import os

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


# Tabla libros de PostgreSQL
class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)


# Datos necesarios para crear un libro
class LibroCreate(BaseModel):
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    anio: int


# Datos que devuelve la API
class LibroResponse(LibroCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD de libros", version="1.0.0")


# Abre y cierra la conexión con la base de datos
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "API de libros funcionando"}


@app.get("/libros", response_model=list[LibroResponse])
def listar_libros(db: Session = Depends(get_db)):
    libros = db.query(Libro).all()

    logger.info("Se ha consultado la lista de libros")

    return libros


@app.get("/libros/{libro_id}", response_model=LibroResponse)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()

    if libro is None:
        logger.warning("Libro no encontrado: %s", libro_id)

        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado",
        )

    logger.info("Se ha consultado el libro %s", libro_id)

    return libro


@app.post(
    "/libros",
    response_model=LibroResponse,
    status_code=status.HTTP_201_CREATED,
)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    nuevo_libro = Libro(
        titulo=libro.titulo,
        autor=libro.autor,
        anio=libro.anio,
    )

    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)

    logger.info("Se ha creado el libro %s", nuevo_libro.id)

    return nuevo_libro


@app.delete(
    "/libros/{libro_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()

    if libro is None:
        logger.warning("Libro no encontrado: %s", libro_id)

        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado",
        )

    db.delete(libro)
    db.commit()

    logger.info("Se ha eliminado el libro %s", libro_id)