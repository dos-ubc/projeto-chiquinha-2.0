from app.database.db import get_db
from app.models.usuario import Usuario

def get_all() -> dict:
    with next(get_db()) as db:
        return db.query(Usuario).all()
    
def add_usuario(nome: str) -> dict:
    with next(get_db()) as db:
        usuario = Usuario(usuario_nome=nome)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario.id

def get_usuario_id(id: int) -> Usuario:
    with next(get_db()) as db:
        return db.query(Usuario).filter(Usuario.id_usuario == id).first()
