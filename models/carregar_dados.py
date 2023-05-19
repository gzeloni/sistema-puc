import json

def carregar_dados():
    try:
        with open("dados.json", "r") as file:
            dados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }
    return dados