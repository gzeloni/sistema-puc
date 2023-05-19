from models.listar_registros import listar_registros
from models.salvar_dados import salvar_dados


def atualizar_registro(chave, dados):
    listar_registros(chave, dados)

    indice = int(input("Digite o índice do registro que deseja atualizar: "))

    if indice >= 0 and indice < len(dados[chave]):
        registro = dados[chave][indice]

        if chave == "estudantes":
            registro["nome"] = input("Digite o nome atualizado do estudante: ")
            registro["matricula"] = input("Digite a matrícula atualizada do estudante: ")
            registro["curso"] = input("Digite o curso atualizado do estudante: ")

        elif chave == "disciplinas":
            registro["codigo"] = input("Digite o código atualizado da disciplina: ")
            registro["nome"] = input("Digite o nome atualizado da disciplina: ")
            registro["professor"] = input("Digite o nome atualizado do professor da disciplina: ")

        elif chave == "professores":
            registro["nome"] = input("Digite o nome atualizado do professor: ")
            registro["disciplinas"] = input("Digite as disciplinas atualizadas do professor: ")

        elif chave == "turmas":
            registro["codigo"] = input("Digite o código atualizado da turma: ")
            registro["disciplina"] = input("Digite a disciplina atualizada da turma: ")
            registro["professor"] = input("Digite o professor atualizado da turma: ")

        elif chave == "matriculas":
            registro["estudante"] = input("Digite o nome atualizado do estudante: ")
            registro["disciplina"] = input("Digite a disciplina atualizada: ")
            registro["turma"] = input("Digite a turma atualizada: ")

        salvar_dados(dados)
        print("Registro atualizado com sucesso.")
    else:
        print("Índice inválido.")