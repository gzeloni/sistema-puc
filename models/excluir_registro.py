# O código a seguir é responsável por excluir um registro com base em um código específico.

# Importa as funções necessárias dos módulos
from models.limpar_tela import limpar_tela
from models.listar_registros import listar_registros
from models.salvar_dados import salvar_dados

# Função para excluir um registro


def excluir_registro(chave, dados, campo_codigo):
    # Limpa a tela
    limpar_tela()
    try:
        # Solicita ao usuário o código do registro a ser excluído, de acordo com o tipo de chave
        codigo = int(
            input(f"Digite o código do(a) {chave[:-1]} que deseja excluir: "))

        # Verifica se a chave existe nos dados e se é uma lista
        if chave in dados and isinstance(dados[chave], list):
            registros = dados[chave]

            indice = None
            # Percorre os registros e busca o índice do registro com o código fornecido
            for i, registro in enumerate(registros):
                if campo_codigo in registro and registro[campo_codigo] == codigo:
                    indice = i
                    break

            # Se o índice foi encontrado, exclui o registro, salva os dados e exibe uma mensagem de sucesso
            if indice is not None:
                del dados[chave][indice]
                salvar_dados(dados)
                limpar_tela()
                print("Registro excluído com sucesso.")
            else:
                print(f"Código do(a) {chave[:-1]} não encontrado.")
        else:
            print("Chave inválida ou lista de registros inexistente.")

    # Trata a exceção caso o usuário digite um valor inválido para o código
    except ValueError:
        print("Digite um código válido (número inteiro).")
    # Trata outras exceções que possam ocorrer durante a exclusão do registro
    except Exception as e:
        print("Ocorreu um erro ao excluir o registro:", e)
