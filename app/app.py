from fastapi import FastAPI
from app.database.db import engine, Base
from app.models.perguntas_respostas import PerguntasRespostas
from app.models.rastreio import Rastreio
from app.models.usuario import Usuario

from app.crud.perguntas_respostas import get_all as perguntas_respostas_all
from app.crud.perguntas_respostas import add_pergunta_resposta
from app.crud.rastreio import add_rastreio
from app.crud.usuario import add_usuario
from app.services.service import ollama_con

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    descrucao_ia: str = """
        Você é um analista de obras musicais e sua missão é tirar dúvidas do usuário.
        
        Nome do usuário: {nome}
        pergunta do usuário: {usuario_pergunta}
        lista de dicionarios onde as keys são perguntas e os values são a respostas: {pergunta_e_respostas_banco}
        
        preciso que compare a pergunta do usuário e as keys da lista de json, após, preciso traga a resposta que é o value,
        faça uma edição da resposta para torna-la mais humanizada, porém só traga a resposta editada, nada mais, também tente incluir 
        o nome do usuário para deixar mais humando
    """
    nome = "Danilo"
    perg = "Que dia hj"
    perguntas_respostas = perguntas_respostas_all()
    resposta = { perguntas_respostas[0].pergunta : perguntas_respostas[0].resposta}

    texto = descrucao_ia.format(
        nome=nome,
        usuario_pergunta=perg,
        pergunta_e_respostas_banco=resposta
    )
    print(texto)

    resposta = ollama_con(texto)
    return {"resposta": resposta}

@app.post("/")
def cadastrar_pergunta():
    x = add_pergunta_resposta("Que dia hj", "dia de trabalhar")
    return "OK"