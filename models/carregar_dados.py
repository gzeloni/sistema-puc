import json

def carregar_dados():
    try:
        with open("dados.json", "r") as file:
            dados = json.load(file)
    except FileNotFoundError:
        print("Arquivo 'dados.json' não encontrado. Criando um novo arquivo vazio.")
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo 'dados.json'. Criando um novo arquivo vazio.")
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }
    except Exception as e:
        print("Ocorreu um erro ao carregar os dados:", e)
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }
    return dados
