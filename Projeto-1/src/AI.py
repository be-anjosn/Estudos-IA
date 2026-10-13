import ollama
from Models import AnaliseFeedback


def passando_pela_IA(argumento):
    mensagem_utilizador = {
    'role': 'user',
    'content': 
    f"""
        Analise o texto e devolva os dados no formato JSON solicitado: {argumento}
    """
    }

    resposta = ollama.chat(
        model='llama3.2:1b', 
        messages=[mensagem_utilizador],
        format=AnaliseFeedback.model_json_schema(),
        options={'temperature': 0.1}
    )

    return resposta['message']['content']

