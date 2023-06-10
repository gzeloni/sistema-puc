from models.listar_registros import listar_registros
from models.salvar_dados import salvar_dados

def excluir_registro(chave, dados):
    try:
        codigo = int(input("Digite o código (RA) do aluno que deseja excluir: "))

        if chave in dados and isinstance(dados[chave], list):
            registros = dados[chave]

            indice = None
            for i, registro in enumerate(registros):
                if "codigo" in registro and registro["codigo"] == codigo:
                    indice = i
                    break

            if indice is not None:
                del dados[chave][indice]
                salvar_dados(dados)
                print("Registro excluído com sucesso.")
            else:
                print("Código do aluno não encontrado.")
        else:
            print("Chave inválida ou lista de registros inexistente.")

    except ValueError:
        print("Digite um código válido (número inteiro).")
    except Exception as e:
        print("Ocorreu um erro ao excluir o registro:", e)
