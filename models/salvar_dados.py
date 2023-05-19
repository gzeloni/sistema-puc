import json

def salvar_dados(registros):
    with open('dados.json', 'w') as arquivo:
        json.dump(registros, arquivo, indent=4)