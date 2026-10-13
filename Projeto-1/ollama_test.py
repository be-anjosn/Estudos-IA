# This file is dedicated to test Ollama locally. If you don't have Ollama downloaded, please check README.txt

import ollama

text_util = {
    'role': 'user',
    'content': 'What is Artificial Intelligence? Answer in one sentence.'
}

# Atualizado para o modelo exato que está a rodar
awnser = ollama.chat(
    model='llama3.2:1b', 
    messages=[text_util]
)

print("Ollama awnser:")
print(awnser['message']['content'])

