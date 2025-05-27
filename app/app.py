from fastapi import FastAPI
from app.database.db import engine, Base
from app.models.perguntas_respostas import PerguntasRespostas
from app.models.rastreio import Rastreio
from app.models.usuario import Usuario
from app.schemas.usuario_interacao import PerguntaBody
from app.schemas.cadastro_pergunta import CadastroPerguntaResposta

from app.crud.perguntas_respostas import get_all as perguntas_respostas_all
from app.crud.perguntas_respostas import add_pergunta_resposta
from app.crud.rastreio import add_rastreio
from app.crud.usuario import add_usuario
from app.services.service import gemini_con

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/perguntar")
def main(dados_pergunta: PerguntaBody):
    descrucao_ia: str = """
        Preciso que só se atente a responder de acordo com as resposta cadastradas aqui no json {pergunta_e_respostas_banco}, não deve buscar nada na sua base de conhecimento.
        
        Você é um analista de obras musicais e sua missão é tirar dúvidas do usuário.

        Nome do usuário: {nome}
        pergunta do usuário: {usuario_pergunta}
        lista de dicionarios onde as keys são perguntas e os values são a respostas: {pergunta_e_respostas_banco}
        
        preciso que compare a pergunta do usuário e as keys da lista de json, após, preciso traga a resposta que é o value,
        faça uma edição da resposta para torna-la mais humanizada, porém só traga a resposta editada, nada mais, abaixo um exemplo:
        
        nome_usuario, resposta

    """
    nome = dados_pergunta.usuario_nome
    pergunta_usuario = dados_pergunta.usuario_pergunta
    perguntas_respostas = perguntas_respostas_all()
    resposta = [ {
        "pergunta": pergunta_resposta.pergunta,
        "resposta": pergunta_resposta.resposta
    } for pergunta_resposta in perguntas_respostas ]

    texto = descrucao_ia.format(
        nome=nome,
        usuario_pergunta=pergunta_usuario,
        pergunta_e_respostas_banco=resposta
    )

    resposta = gemini_con(texto)
    return {"resposta": resposta}

@app.post("/cadastro-pergunta-resposta")
def cadastrar_pergunta(dados_cadastro_pergunta_resposta: CadastroPerguntaResposta) -> None:
    dados = dados_cadastro_pergunta_resposta
    add_pergunta_resposta(dados.pergunta, dados.resposta)
    return 200