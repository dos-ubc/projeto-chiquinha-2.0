from ollama import Client

client = Client(host="http://ollama:11434")

def ollama_con(mensagem: str):
    model = 'phi4-mini:3.8b'
    resposta = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )
    return resposta['message']['content']