from pydantic import BaseModel


class CadastroPerguntaResposta(BaseModel):
    usuario: str
    pergunta: str
    resposta: str
