import ollama

mensagem_utilizador = {
    'role': 'user',
    'content': 'O que é a Inteligência Artificial? Responda numa frase.'
}

# Atualizado para o modelo exato que está a rodar
resposta = ollama.chat(
    model='llama3.1:8b', 
    messages=[mensagem_utilizador]
)

print("Resposta do Ollama:")
print(resposta['message']['content'])