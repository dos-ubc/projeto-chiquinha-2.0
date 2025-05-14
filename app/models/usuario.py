from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'USUARIO'.lower()
    id_usuario: Integer = Column('id_usuario', Integer, primary_key=True, autoincrement=True, nullable=False)
    usuario_nome: str = Column('usuario_nome', String(100))
    data_criacao: DateTime = Column('data_criacao', DateTime, default=datetime.now)
