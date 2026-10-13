import csv
import Models
from pydantic import ValidationError
from AI import passando_pela_IA


arquivo_origem = "../data/feedbacks_entrada.csv"
lista_feedbacks=[]
with open(arquivo_origem, mode="r", encoding="utf-8") as file_in:
    leitor = csv.DictReader(file_in, delimiter=",")
    for linha in leitor:
        try:
            resposta_texto = passando_pela_IA(linha)
            dados = Models.AnaliseFeedback.model_validate_json(resposta_texto)
            lista_feedbacks.append(dados.model_dump())
        except ValidationError as e:
            print("\n❌ O Pydantic bloqueou a IA! Capturamos o seguinte erro:")
            print(e)
            continue


arquivo_destino="../data/feedbacks_saida.csv"
with open(arquivo_destino, mode="w", encoding="utf-8") as file_out:
    cabecalhos_origem = ["sentimento", "nota_atendimento", "resumo_curto"]
    escritor_mock = csv.DictWriter(file_out, fieldnames=cabecalhos_origem)
    escritor_mock.writeheader()
    escritor_mock.writerows(lista_feedbacks)

