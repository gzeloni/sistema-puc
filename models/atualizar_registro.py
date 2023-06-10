from models.formatar_cpf import formatar_cpf
from models.listar_registros import listar_registros
from models.salvar_dados import salvar_dados
from models.trim_string import trim_string

def atualizar_registro(chave, dados):
    try:
        codigo = int(input("Digite o código do estudante que deseja atualizar: "))

        if chave in dados and isinstance(dados[chave], list):
            registros = dados[chave]

            indice = None
            for i, registro in enumerate(registros):
                if "codigo" in registro and registro["codigo"] == codigo:
                    indice = i
                    break

            if indice is not None:
                registro = dados[chave][indice]

                if chave == "estudantes":
                    registro["nome"] = trim_string(input("Digite o nome atualizado do estudante: "))
                    registro["CPF"] = formatar_cpf(input("Digite o CPF do estudante: "))

                elif chave == "disciplinas":
                    registro["codigo"] = trim_string(input("Digite o código atualizado da disciplina: "))
                    registro["nome"] = trim_string(input("Digite o nome atualizado da disciplina: "))
                    registro["professor"] = trim_string(input("Digite o nome atualizado do professor da disciplina: "))

                elif chave == "professores":
                    registro["nome"] = trim_string(input("Digite o nome atualizado do professor: "))
                    registro["disciplinas"] = trim_string(input("Digite as disciplinas atualizadas do professor: "))

                elif chave == "turmas":
                    registro["codigo"] = trim_string(input("Digite o código atualizado da turma: "))
                    registro["disciplina"] = trim_string(input("Digite a disciplina atualizada da turma: "))
                    registro["professor"] = trim_string(input("Digite o professor atualizado da turma: "))

                elif chave == "matriculas":
                    registro["estudante"] = trim_string(input("Digite o nome atualizado do estudante: "))
                    registro["disciplina"] = trim_string(input("Digite a disciplina atualizada: "))
                    registro["turma"] = trim_string(input("Digite a turma atualizada: "))

                salvar_dados(dados)
                print("Registro atualizado com sucesso.")
            else:
                print("Código do estudante não encontrado.")
        else:
            print("Chave inválida ou lista de registros inexistente.")
    except Exception as e:
        print("Ocorreu um erro ao atualizar o registro:", e)
