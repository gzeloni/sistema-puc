from models.listar_registros import listar_registros  # Importa a função listar_registros do módulo models.listar_registros
from models.salvar_dados import salvar_dados  # Importa a função salvar_dados do módulo models.salvar_dados

def excluir_registro(chave, dados):
    codigo = int(input("Digite o código (RA) do aluno que deseja excluir: "))  # Solicita ao usuário o código do aluno que deseja excluir

    if chave in dados and isinstance(dados[chave], list):
        registros = dados[chave]  # Obtém a lista de registros da chave especificada

        # Procura o registro pelo código do aluno
        indice = None
        for i, registro in enumerate(registros):
            if "codigo" in registro and registro["codigo"] == codigo:
                indice = i
                break

        if indice is not None:
            del dados[chave][indice]  # Remove o registro da lista de registros da chave especificada
            salvar_dados(dados)  # Chama a função salvar_dados para salvar as alterações nos dados
            print("Registro excluído com sucesso.")  # Exibe uma mensagem informando que o registro foi excluído com sucesso
        else:
            print("Código do aluno não encontrado.")  # Exibe uma mensagem informando que o código do aluno não foi encontrado
    else:
        print("Chave inválida ou lista de registros inexistente.")  # Exibe uma mensagem informando que a chave é inválida ou a lista de registros não existe
