from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy import Column, Integer, DateTime


Base = declarative_base()

class PeguntasRespostas(Base):
    __tablename__ = 'PERGUNTAS_RESPOSTAS'.lower()
    id: Integer = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    pergunta: String = Column('pergunta', String(200))
    resposta: String = Column('resposta', String(200))
    data_cadastro: DateTime = Column('data_cadastro', DateTime, default=datetime.now())
