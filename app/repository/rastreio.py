from sqlalchemy.orm import base
from sqlalchemy.types import Integer, String, DateTime


class Rastreio(base):
    id: Integer
    id_usuario: Integer
    id_pergunta: Integer
    data: DateTime
