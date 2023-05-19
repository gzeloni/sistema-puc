from models.listar_registros import listar_registros
from models.salvar_dados import salvar_dados

def excluir_registro(chave, dados):
    listar_registros(chave, dados)

    indice = int(input("Digite o índice do registro que deseja excluir: "))

    if indice >= 0 and indice < len(dados[chave]):
        del dados[chave][indice]
        salvar_dados(dados)
        print("Registro excluído com sucesso.")
    else:
        print("Índice inválido.")