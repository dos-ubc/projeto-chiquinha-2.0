from sqlalchemy.orm import base
from sqlalchemy.types import Integer, String, DateTime


class PeguntasRespostas(base):
    id: Integer
    pergunta: String
    resposta: String
    dataCadastro: DateTime