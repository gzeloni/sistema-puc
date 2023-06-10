import json

def salvar_dados(registros):
    try:
        with open('dados.json', 'w') as arquivo:
            json.dump(registros, arquivo, indent=4)
        print("Dados salvos com sucesso.")
    except IOError:
        print("Erro ao salvar os dados. Verifique as permissões do arquivo ou o caminho fornecido.")
    except Exception as e:
        print("Ocorreu um erro ao salvar os dados:", e)
