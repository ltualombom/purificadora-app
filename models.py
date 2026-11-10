from sqlalchemy import Column, Float, Integer, String, Text
from database import Base


class ClienteDB(Base):
  __tablename__ = "clientes"
  id = Column(Integer, primary_key=True, index=True)
  nombre = Column(String, index=True)
  telefono = Column(String)
  direccion = Column(String)
  saldo_dinero = Column(Float, default=0.0)
  botellones_prestados = Column(Integer, default=0)


class ProductoDB(Base):
  __tablename__ = "productos"
  id = Column(Integer, primary_key=True, index=True)
  nombre = Column(String, unique=True)
  stock = Column(Integer, default=0)
  minimo = Column(Integer, default=5)
  precio = Column(Float, default=0.0)


class MovimientoDB(Base):
  __tablename__ = "movimientos"
  id = Column(Integer, primary_key=True, index=True)
  tipo = Column(String)
  categoria = Column(String)
  monto = Column(Float)
  descripcion = Column(Text)
  fecha = Column(String)
