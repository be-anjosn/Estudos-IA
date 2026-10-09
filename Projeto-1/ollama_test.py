#
#git add Projeto-1/
#git commit -m "Sua mensagem sobre o que mudou no projeto"
#git push origin main#
# 

import ollama

mensagem_utilizador = {
    'role': 'user',
    'content': 'O que é a Inteligência Artificial? Responda numa frase.'
}

# Atualizado para o modelo exato que está a rodar
resposta = ollama.chat(
    model='llama3.2:1b', 
    messages=[mensagem_utilizador]
)

print("Resposta do Ollama:")
print(resposta['message']['content'])