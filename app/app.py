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
    descrucao_ia: str = """
        Você um analista de obras músicais e sua missão é tirar dúvidas do usuário,
        vou te fornesser uma lista de perguntas e respostas em formato json, preciso que compare a pergunta 
        do usuário com as perguntas do json, caso a veja uma semelhança, devolva a resposta de acordo com a pergunta,
        o json é uma lista de perguntas e respostas com ]
        [{"pergunta": ..., "resposta": ...}], também preciso que formule a resposta de forma dinâmica, para tornar o texto
        mais humanizado e interativo.
        segue a pergunta do usuário: {}
        pergunta do usuario: {}
        segue a json com lista de pergunta e respostas
    """
    nome = "danilo"
    perg = "Que dia é hoje?"
    perguntas_respostas = perguntas_respostas_all()
    texto = f"Compare essa pergunta: {perg} com as perguntas desse JSON {perguntas_respostas} e me traga a resposta do JSON, por favor, meu nome é: {nome}"
    resposta = ollama_con(texto) 
    return {"resposta": resposta}
