import json  # Importa o módulo json

def carregar_dados():
    try:
        with open("dados.json", "r") as file:  # Abre o arquivo "dados.json" em modo de leitura
            dados = json.load(file)  # Carrega os dados do arquivo usando a função json.load()
    except (FileNotFoundError, json.JSONDecodeError):  # Trata as exceções FileNotFoundError e JSONDecodeError
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }  # Define um dicionário vazio com as chaves "estudantes", "disciplinas", "professores", "turmas" e "matriculas"
    return dados  # Retorna os dados carregados do arquivo ou o dicionário vazio em caso de erro