# O código a seguir é responsável por incluir um novo registro em um dicionário de dados, com base na chave fornecida.

# Importação dos módulos necessários
from models.formatar_cpf import formatar_cpf
from models.limpar_tela import limpar_tela
from models.salvar_dados import salvar_dados
from models.trim_string import trim_string
from models.validacoes import validar_codigo

# Função para incluir um novo registro


def incluir_registro(chave, dados):
    limpar_tela()
    try:
        # Obtém a lista de registros com base na chave fornecida
        registros = dados.get(chave, [])
        novo_registro = {}

        # Verifica a chave fornecida e solicita os dados apropriados para cada tipo de registro
        if chave == "estudantes":
            novo_registro["codigo"] = int(
                input("Digite o código do estudante (RA): "))
            novo_registro["nome"] = trim_string(
                input("Digite o nome do estudante: "))
            novo_registro["cpf"] = formatar_cpf(
                trim_string(input("Digite o CPF do estudante: ")))

        elif chave == "disciplinas":
            novo_registro["codigo"] = int(
                input("Digite o código da disciplina: "))
            novo_registro["nome"] = trim_string(
                input("Digite o nome da disciplina: "))

        elif chave == "professores":
            novo_registro["codigo"] = int(
                input("Digite o código do professor: "))
            novo_registro["nome"] = trim_string(
                input("Digite o nome do professor: "))
            novo_registro["cpf"] = formatar_cpf(
                trim_string(input("Digite o CPF do professor: ")))

        elif chave == "turmas":
            novo_registro["codigo"] = int(input("Digite o código da turma: "))
            novo_registro["cod_professor"] = int(
                input("Digite o código do professor: "))
            novo_registro["cod_disciplina"] = int(
                input("Digite o código da disciplina: "))

            # Valida o código do professor e da disciplina antes de incluir a turma
            if not validar_codigo(novo_registro["cod_professor"], "professores", dados):
                print("Erro: código do professor inválido. O professor não existe.")
                return

            if not validar_codigo(novo_registro["cod_disciplina"], "disciplinas", dados):
                print("Erro: código da disciplina inválido. A disciplina não existe.")
                return

        elif chave == "matriculas":
            novo_registro["codigo"] = int(
                input("Digite o código da matricula: "))
            novo_registro["cod_turma"] = int(
                input("Digite o código da turma: "))
            novo_registro["codigo"] = int(
                input("Digite o código do estudante (RA): "))

            # Valida o código da turma e do estudante antes de incluir a matrícula
            if not validar_codigo(novo_registro["cod_turma"], "turmas", dados):
                print("Erro: código da turma inválido. A turma não existe.")
                return

            if not validar_codigo(novo_registro["codigo"], "estudantes", dados):
                print("Erro: código do estudante inválido. O estudante não existe.")
                return

        # Adiciona o novo registro à lista de registros
        registros.append(novo_registro)
        dados[chave] = registros
        salvar_dados(dados)
        limpar_tela()
        print("Registro incluído com sucesso.")

    # Trata a exceção de valor inválido
    except ValueError:
        print("Erro: entrada inválida. Certifique-se de fornecer um valor válido para as informações solicitadas.")

    # Trata outras exceções que possam ocorrer durante a inclusão do registro
    except Exception as e:
        print("Ocorreu um erro ao incluir o registro:", e)
