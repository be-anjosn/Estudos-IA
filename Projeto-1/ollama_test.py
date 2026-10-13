# This file is dedicated to test Ollama locally. If you don't have Ollama downloaded, please try the followin lines:

### 1. Install Ollama
#- **macOS / Windows**: Download the installer directly from https://ollama.com/download.
#- **Linux**: Run the official installation script:
#  bash curl -fsSL https://ollama.com/install.sh | sh

### Pull and chat with a lightweight test model (e.g., Llama 3.2 1B or 3B)
# ollama run llama3.2:1b

# Basic Commands:
#ollama list      # List models downloaded locally
#ollama ps        # Show models currently loaded in memory
#ollama rm <name> # Remove a model


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

