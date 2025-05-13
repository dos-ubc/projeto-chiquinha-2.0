FROM ollama/ollama:latest

RUN ollama pull llama3.3
EXPOSE 11434


CMD /bin/sh -c "ollama serve && ollama pull llama3.1"