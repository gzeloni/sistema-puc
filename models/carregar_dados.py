# O código a seguir é responsável por carregar os dados de um arquivo JSON.

# Importa a biblioteca JSON para trabalhar com arquivos JSON
import json

# Função para carregar os dados de um arquivo JSON


def carregar_dados():
    try:
        # Tenta abrir o arquivo 'dados.json' em modo de leitura
        with open("dados.json", "r") as file:
            # Carrega os dados do arquivo JSON para a variável 'dados'
            dados = json.load(file)

    # Se o arquivo 'dados.json' não for encontrado, cria um novo arquivo vazio
    except FileNotFoundError:
        print("Arquivo 'dados.json' não encontrado. Criando um novo arquivo vazio.")
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }

    # Se houver um erro ao decodificar o arquivo JSON, cria um novo arquivo vazio
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo 'dados.json'. Criando um novo arquivo vazio.")
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }

    # Se ocorrer qualquer outra exceção, exibe uma mensagem de erro e cria um novo arquivo vazio
    except Exception as e:
        print("Ocorreu um erro ao carregar os dados:", e)
        dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
        }

    # Retorna os dados carregados (ou o novo arquivo vazio)
    return dados
