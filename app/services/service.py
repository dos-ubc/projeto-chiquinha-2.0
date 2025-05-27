import requests
import os

# Coloque sua chave aqui ou use variável de ambiente
API_KEY = "AIzaSyBsMcuyWrLaGXaejbvHJ7MChceyCF_hvxk"#os.getenv("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
MODEL = "gemini-1.5-flash"  # ou "gemini-1.5-pro"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

def gemini_con(mensagem: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": mensagem
                    }
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(ENDPOINT, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "Erro ao interpretar a resposta do Gemini."
    else:
        return f"Erro {response.status_code}: {response.text}"
