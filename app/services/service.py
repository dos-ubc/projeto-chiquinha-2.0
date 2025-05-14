import ollama

ollama.base_url = "http://localhost:11434"
def  ollama_con(mensagem: str):
    model: str = 'llama3'
    resposta = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )
    return resposta['message']['content']