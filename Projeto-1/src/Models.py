from pydantic import BaseModel, Field
from typing import Literal

class AnaliseFeedback(BaseModel):
    sentimento: Literal["positivo","negativo", "neutro"]
    nota_atendimento: int = Field(
        ge=1,
        le=5,
        description="Nota de que representa o nível de satisfação do cliente, sendo 1 - muito insatisfeito e 5 - muito satisfeito"
    )
    resumo_curto: str = Field( 
        description="Um resumo curto em 1 linha sobre o assunto"
    )

import ollama
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

#resposta_texto = passando_pela_IA(dados)
#dados = AnaliseFeedback.model_validate_json(resposta_texto)
# dados -> objeto de AnaliseFeedback

import csv
import os
arquivo_origem = "../data/feedbacks_entrada.csv"
lista_feedbacks=[]
with open(arquivo_origem, mode="r", encoding="utf-8") as file_in:
    leitor = csv.DictReader(file_in, delimiter=",")
    for linha in leitor:
        resposta_texto = passando_pela_IA(linha)
        dados = AnaliseFeedback.model_validate_json(resposta_texto)
        lista_feedbacks.append(dados.model_dump())

print(lista_feedbacks)

arquivo_destino="../data/feedbacks_saida.csv"
with open(arquivo_destino, mode="w", encoding="utf-8") as file_out:
    cabecalhos_origem = ["sentimento", "nota_atendimento", "resumo_curto"]
    escritor_mock = csv.DictWriter(file_out, fieldnames=cabecalhos_origem)
    escritor_mock.writeheader()
    escritor_mock.writerows(lista_feedbacks)