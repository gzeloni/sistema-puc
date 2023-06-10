from models.formatar_cpf import formatar_cpf
from models.salvar_dados import salvar_dados
from models.trim_string import trim_string
from models.validar_numero import validar_numero

def incluir_registro(chave, dados):
    try:
        registros = dados.get(chave, [])
        novo_registro = {}

        if chave == "estudantes":
            novo_registro["codigo"] = int(input("Digite o código do estudante (RA): "))
            novo_registro["nome"] = trim_string(input("Digite o nome do estudante: "))
            novo_registro["cpf"] = formatar_cpf(trim_string(input("Digite o CPF do estudante: ")))

        elif chave == "disciplinas":
            novo_registro["nome"] = trim_string(input("Digite o nome da disciplina: "))
            novo_registro["codigo"] = trim_string(input("Digite o código da disciplina: "))
            while not validar_numero(novo_registro["codigo"]):
                print("Erro: código da disciplina inválido. Digite um valor numérico.")
                novo_registro["codigo"] = trim_string(input("Digite o código da disciplina: "))
            novo_registro["carga_horaria"] = int(input("Digite a carga horária da disciplina: "))

        elif chave == "professores":
            novo_registro["nome"] = trim_string(input("Digite o nome do professor: "))
            novo_registro["departamento"] = trim_string(input("Digite o departamento do professor: "))
            novo_registro["email"] = trim_string(input("Digite o email do professor: "))

        elif chave == "turmas":
            novo_registro["codigo"] = trim_string(input("Digite o código da turma: "))
            while not validar_numero(novo_registro["codigo"]):
                print("Erro: código da turma inválido. Digite um valor numérico.")
                novo_registro["codigo"] = trim_string(input("Digite o código da turma: "))
            novo_registro["disciplina"] = trim_string(input("Digite a disciplina da turma: "))
            novo_registro["professor"] = trim_string(input("Digite o professor da turma: "))

        elif chave == "matriculas":
            novo_registro["estudante"] = trim_string(input("Digite o nome do estudante: "))
            novo_registro["turma"] = trim_string(input("Digite o código da turma: "))
            while not validar_numero(novo_registro["turma"]):
                print("Erro: código da turma inválido. Digite um valor numérico.")
                novo_registro["turma"] = trim_string(input("Digite o código da turma: "))
            novo_registro["status"] = trim_string(input("Digite o status da matrícula: "))

        registros.append(novo_registro)
        dados[chave] = registros
        salvar_dados(dados)
        print("Registro incluído com sucesso.")

    except ValueError:
        print("Erro: entrada inválida. Certifique-se de fornecer um valor válido para as informações solicitadas.")

    except Exception as e:
        print("Ocorreu um erro ao incluir o registro:", e)
