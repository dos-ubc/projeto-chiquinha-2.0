from app.database.db import get_db
from app.models.rastreio import Rastreio

def get_all() -> dict:
    with next(get_db()) as db:
        return db.query(Rastreio).all

def get_rastreio_id(id: int) -> Rastreio:
    with next(get_db()) as db:
        return db.query(Rastreio).filter(Rastreio.id == id).first()

def add_rastreio(id_usuario: int, id_pergunta: int) -> dict:
    with next(get_db()) as db:
        rastreio = Rastreio(id_usuario=id_usuario, id_pergunta=id_pergunta)
        db.add(rastreio)
        db.commit()
        db.refresh(rastreio)
        return rastreio.id
