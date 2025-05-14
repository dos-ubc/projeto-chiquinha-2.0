from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime

Base = declarative_base()

class Rastreio(Base):
    __tablename__ = 'RASTREIO'.lower()
    __table_args__ = {'schema': 'OHRA'}
    id: Integer = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    id_usuario: Integer = Column('id_usuario', Integer)
    id_pergunta: Integer = Column('id_pergunta', Integer)
    data_registro: DateTime = Column('data_registro', DateTime, default=datetime.now)
