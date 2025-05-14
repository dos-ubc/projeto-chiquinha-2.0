from fastapi import FastAPI

from app.crud.perguntas_respostas import get_all as perguntas_respostas_all
from app.crud.rastreio import add_rastreio
from app.crud.usuario import add_usuario
from app.services.service import ollama_con

app = FastAPI()

@app.get("/")
def home():
    nome = "danilo"
    perg = "Que dia é hoje?"
    perguntas_respostas = perguntas_respostas_all()
    texto = f"Comparece essa pergunta: {perg} com as perguntas desse json {perguntas_respostas} e me trada a resposta do json, por favor, meu nome é : {nome}"
    reposta = ollama_con(texto)
    
    return reposta