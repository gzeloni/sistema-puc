from models.salvar_dados import salvar_dados

def incluir_registro(chave, dados):
    registros = dados.get(chave, [])
    novo_registro = {}

    if chave == "estudantes":
        novo_registro["nome"] = input("Digite o nome do estudante: ")
        novo_registro["idade"] = int(input("Digite a idade do estudante: "))
        novo_registro["matricula"] = input("Digite a matrícula do estudante: ")
    elif chave == "disciplinas":
        novo_registro["nome"] = input("Digite o nome da disciplina: ")
        novo_registro["codigo"] = input("Digite o código da disciplina: ")
        novo_registro["carga_horaria"] = int(input("Digite a carga horária da disciplina: "))
    elif chave == "professores":
        novo_registro["nome"] = input("Digite o nome do professor: ")
        novo_registro["departamento"] = input("Digite o departamento do professor: ")
        novo_registro["email"] = input("Digite o email do professor: ")
    elif chave == "turmas":
        novo_registro["codigo"] = input("Digite o código da turma: ")
        novo_registro["disciplina"] = input("Digite a disciplina da turma: ")
        novo_registro["professor"] = input("Digite o professor da turma: ")
    elif chave == "matriculas":
        novo_registro["estudante"] = input("Digite o nome do estudante: ")
        novo_registro["turma"] = input("Digite o código da turma: ")
        novo_registro["status"] = input("Digite o status da matrícula: ")
    
    registros.append(novo_registro)
    dados[chave] = registros
    salvar_dados(dados)
    print("Registro incluído com sucesso.")