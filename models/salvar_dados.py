import json


def salvar_dados(registros):
    try:
        # Abre o arquivo 'dados.json' em modo de escrita e utiliza a função json.dump() para salvar os registros nele
        with open('dados.json', 'w') as arquivo:
            # O parâmetro 'indent=4' é utilizado para adicionar espaçamento e tornar o arquivo JSON mais legível
            json.dump(registros, arquivo, indent=4)

        print("Dados salvos com sucesso.")
    except IOError:
        # Se ocorrer um erro de E/S (Input/Output), exibe uma mensagem indicando o problema
        print("Erro ao salvar os dados. Verifique as permissões do arquivo ou o caminho fornecido.")

    except Exception as e:
        # Captura qualquer outra exceção que ocorrer durante o processo de salvar os dados e exibe uma mensagem de erro junto com a descrição da exceção
        print("Ocorreu um erro ao salvar os dados:", e)
