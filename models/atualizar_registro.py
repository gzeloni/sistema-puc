from models.formatar_cpf import formatar_cpf
from models.listar_registros import listar_registros  # Importa a função listar_registros do módulo models.listar_registros
from models.salvar_dados import salvar_dados  # Importa a função salvar_dados do módulo models.salvar_dados

def atualizar_registro(chave, dados):
    codigo = int(input("Digite o código do estudante que deseja atualizar: "))  # Solicita ao usuário o código do estudante que deseja atualizar

    if chave in dados and isinstance(dados[chave], list):
        registros = dados[chave]  # Obtém a lista de registros da chave especificada

        # Procura o registro pelo código do estudante
        indice = None
        for i, registro in enumerate(registros):
            if "codigo" in registro and registro["codigo"] == codigo:
                indice = i
                break

        if indice is not None:
            registro = dados[chave][indice]  # Obtém o registro correspondente ao índice

            if chave == "estudantes":  # Se a chave for "estudantes"
                registro["nome"] = input("Digite o nome atualizado do estudante: ")  # Solicita ao usuário o nome atualizado do estudante
                registro["CPF"] = formatar_cpf(input("Digite o CPF do estudante: "))  # Solicita ao usuário o CPF atualizado do estudante

            elif chave == "disciplinas":  # Se a chave for "disciplinas"
                registro["codigo"] = input("Digite o código atualizado da disciplina: ")  # Solicita ao usuário o código atualizado da disciplina
                registro["nome"] = input("Digite o nome atualizado da disciplina: ")  # Solicita ao usuário o nome atualizado da disciplina
                registro["professor"] = input("Digite o nome atualizado do professor da disciplina: ")  # Solicita ao usuário o nome atualizado do professor da disciplina

            elif chave == "professores":  # Se a chave for "professores"
                registro["nome"] = input("Digite o nome atualizado do professor: ")  # Solicita ao usuário o nome atualizado do professor
                registro["disciplinas"] = input("Digite as disciplinas atualizadas do professor: ")  # Solicita ao usuário as disciplinas atualizadas do professor

            elif chave == "turmas":  # Se a chave for "turmas"
                registro["codigo"] = input("Digite o código atualizado da turma: ")  # Solicita ao usuário o código atualizado da turma
                registro["disciplina"] = input("Digite a disciplina atualizada da turma: ")  # Solicita ao usuário a disciplina atualizada da turma
                registro["professor"] = input("Digite o professor atualizado da turma: ")  # Solicita ao usuário o professor atualizado da turma

            elif chave == "matriculas":  # Se a chave for "matriculas"
                registro["estudante"] = input("Digite o nome atualizado do estudante: ")  # Solicita ao usuário o nome atualizado do estudante
                registro["disciplina"] = input("Digite a disciplina atualizada: ")  # Solicita ao usuário a disciplina atualizada
                registro["turma"] = input("Digite a turma atualizada: ")  # Solicita ao usuário a turma atualizada

            salvar_dados(dados)  # Chama a função salvar_dados para salvar as alterações nos dados
            print("Registro atualizado com sucesso.")  # Exibe uma mensagem informando que o registro foi atualizado com sucesso
        else:
            print("Código do estudante não encontrado.")  # Exibe uma mensagem informando que o código do estudante não foi encontrado
    else:
        print("Chave inválida ou lista de registros inexistente.")  # Exibe uma mensagem informando que a chave é inválida ou a lista de registros não existe
