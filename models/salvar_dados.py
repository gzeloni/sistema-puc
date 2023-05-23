import json

def salvar_dados(registros):
    with open('dados.json', 'w') as arquivo:  # Abre o arquivo 'dados.json' em modo de escrita
        json.dump(registros, arquivo, indent=4)  # Salva os registros no arquivo no formato JSON com indentação de 4 espaços