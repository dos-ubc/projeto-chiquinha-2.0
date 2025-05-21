from pydantic import BaseModel

class PerguntaBody(BaseModel):
    usuario_nome: str
    usuario_pergunta: str