from models.listar_registros import listar_registros  # Importa a função listar_registros do módulo models.listar_registros
from models.salvar_dados import salvar_dados  # Importa a função salvar_dados do módulo models.salvar_dados

def excluir_registro(chave, dados):
    listar_registros(chave, dados)  # Chama a função listar_registros para exibir os registros da chave especificada

    indice = int(input("Digite o índice do registro que deseja excluir: "))  # Solicita ao usuário o índice do registro que deseja excluir

    if indice >= 0 and indice < len(dados[chave]):  # Verifica se o índice é válido para a chave especificada
        del dados[chave][indice]  # Remove o registro da lista de registros da chave especificada
        salvar_dados(dados)  # Chama a função salvar_dados para salvar as alterações nos dados
        print("Registro excluído com sucesso.")  # Exibe uma mensagem informando que o registro foi excluído com sucesso
    else:
        print("Índice inválido.")  # Exibe uma mensagem informando que o índice é inválido