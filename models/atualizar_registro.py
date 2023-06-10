# O código a seguir implementa uma função chamada atualizar_registro(),
# que é responsável por atualizar um registro em um dicionário de dados.

# Importa as funções necessárias para o programa
from models.formatar_cpf import formatar_cpf
from models.limpar_tela import limpar_tela
from models.listar_registros import listar_registros
from models.salvar_dados import salvar_dados
from models.trim_string import trim_string

# Função para atualizar um registro no dicionário de dados


def atualizar_registro(chave, dados):
    # Limpa a tela do console
    limpar_tela()

    try:
        # Solicita o código a ser atualizado
        codigo = int(input(
            "Digite o código do(a) {} que deseja editar: ".format(
                "estudante" if chave == "estudantes" else
                "disciplina" if chave == "disciplinas" else
                "professor" if chave == "professores" else
                "turma" if chave == "turmas" else
                "matrícula"
            )
        ))

        # Verifica se a chave existe nos dados e se é uma lista de registros
        if chave in dados and isinstance(dados[chave], list):
            registros = dados[chave]

            indice = None
            for i, registro in enumerate(registros):
                # Procura pelo registro com o código correspondente
                if "codigo" in registro and registro["codigo"] == codigo:
                    indice = i
                    break

            if indice is not None:
                # Obtém o registro a ser atualizado
                registro = dados[chave][indice]

                # Atualiza os campos do registro com base na chave
                if chave == "estudantes":
                    registro["nome"] = trim_string(
                        input("Digite o nome atualizado do estudante: "))
                    registro["CPF"] = formatar_cpf(
                        input("Digite o CPF do estudante: "))

                elif chave == "disciplinas":
                    registro["codigo"] = trim_string(
                        input("Digite o código atualizado da disciplina: "))
                    registro["nome"] = trim_string(
                        input("Digite o nome atualizado da disciplina: "))
                    registro["professor"] = trim_string(
                        input("Digite o nome atualizado do professor da disciplina: "))

                elif chave == "professores":
                    registro["nome"] = trim_string(
                        input("Digite o nome atualizado do professor: "))
                    registro["disciplinas"] = trim_string(
                        input("Digite as disciplinas atualizadas do professor: "))

                elif chave == "turmas":
                    registro["codigo"] = trim_string(
                        input("Digite o código atualizado da turma: "))
                    registro["disciplina"] = trim_string(
                        input("Digite a disciplina atualizada da turma: "))
                    registro["professor"] = trim_string(
                        input("Digite o professor atualizado da turma: "))

                elif chave == "matriculas":
                    registro["estudante"] = trim_string(
                        input("Digite o nome atualizado do estudante: "))
                    registro["disciplina"] = trim_string(
                        input("Digite a disciplina atualizada: "))
                    registro["turma"] = trim_string(
                        input("Digite a turma atualizada: "))

                # Salva os dados atualizados no arquivo
                salvar_dados(dados)
                limpar_tela()
                print("Registro atualizado com sucesso.")
            else:
                print("Código não encontrado.")
        else:
            print("Chave inválida ou lista de registros inexistente.")
    except Exception as e:
        print("Ocorreu um erro ao atualizar o registro:", e)
