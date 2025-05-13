from sqlalchemy.orm import base
from sqlalchemy.types import Integer, String, DateTime


class Usuario(base):
    id_usuario: Integer
    usuario_nome: str
    data_interacao: DateTime
