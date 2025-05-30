from app.database.db import get_db
from app.models.perguntas_respostas import PerguntasRespostas

def get_all() -> dict:
    with next(get_db()) as db:
        return db.query(PerguntasRespostas).all()

def add_pergunta_resposta(pergunta: str, resposta: str) -> dict:
    with next(get_db()) as db:
        pergunta_resposta = PerguntasRespostas(pergunta=pergunta, resposta=resposta)
        db.add(pergunta_resposta)
        db.commit()
        db.refresh(pergunta_resposta)
        return pergunta_resposta.id
