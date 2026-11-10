from database import SessionLocal, engine
import models
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AquaControl API")

# Sirve la interfaz web en la ruta /app
app.mount("/app", StaticFiles(directory="static", html=True), name="static")


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


class ClienteCreate(BaseModel):
  nombre: str
  telefono: str
  direccion: str


@app.get("/api/clientes")
def listar_clientes(db: Session = Depends(get_db)):
  return db.query(models.ClienteDB).all()


@app.post("/api/clientes")
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
  db_cliente = models.ClienteDB(**cliente.dict())
  db.add(db_cliente)
  db.commit()
  db.refresh(db_cliente)
  return db_cliente
