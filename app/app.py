from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker, declarative_base
from app.models.pergunas_respostas import PeguntasRespostas
from fastapi import FastAPI
from app.models.rastreio import Rastreio
from app.models.usuario import Usuario

from app.crud.perguntas_respostas import get_all as perguntas_respostas_all
from app.crud.rastreio import add_rastreio
from app.crud.usuario import add_usuario
from app.services.service import ollama_con
from app.database.db import engine
from app.database.db import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    nome = "danilo"
    perg = "Que dia é hoje?"
    perguntas_respostas = perguntas_respostas_all()
    texto = f"Compare essa pergunta: {perg} com as perguntas desse JSON {perguntas_respostas} e me traga a resposta do JSON, por favor, meu nome é: {nome}"
    resposta = ollama_con(texto) 
    return {"resposta": resposta}
