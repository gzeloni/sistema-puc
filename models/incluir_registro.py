from models.salvar_dados import salvar_dados  # Importa a função salvar_dados do módulo models.salvar_dados

def incluir_registro(chave, dados):
    registros = dados.get(chave, [])  # Obtém a lista de registros da chave especificada ou retorna uma lista vazia se a chave não existir
    novo_registro = {}  # Cria um novo dicionário para armazenar o registro

    if chave == "estudantes":  # Se a chave for "estudantes"
        novo_registro["nome"] = input("Digite o nome do estudante: ")  # Solicita ao usuário o nome do estudante
        novo_registro["idade"] = int(input("Digite a idade do estudante: "))  # Solicita ao usuário a idade do estudante
        novo_registro["matricula"] = input("Digite a matrícula do estudante: ")  # Solicita ao usuário a matrícula do estudante
    elif chave == "disciplinas":  # Se a chave for "disciplinas"
        novo_registro["nome"] = input("Digite o nome da disciplina: ")  # Solicita ao usuário o nome da disciplina
        novo_registro["codigo"] = input("Digite o código da disciplina: ")  # Solicita ao usuário o código da disciplina
        novo_registro["carga_horaria"] = int(input("Digite a carga horária da disciplina: "))  # Solicita ao usuário a carga horária da disciplina
    elif chave == "professores":  # Se a chave for "professores"
        novo_registro["nome"] = input("Digite o nome do professor: ")  # Solicita ao usuário o nome do professor
        novo_registro["departamento"] = input("Digite o departamento do professor: ")  # Solicita ao usuário o departamento do professor
        novo_registro["email"] = input("Digite o email do professor: ")  # Solicita ao usuário o email do professor
    elif chave == "turmas":  # Se a chave for "turmas"
        novo_registro["codigo"] = input("Digite o código da turma: ")  # Solicita ao usuário o código da turma
        novo_registro["disciplina"] = input("Digite a disciplina da turma: ")  # Solicita ao usuário a disciplina da turma
        novo_registro["professor"] = input("Digite o professor da turma: ")  # Solicita ao usuário o professor da turma
    elif chave == "matriculas":  # Se a chave for "matriculas"
        novo_registro["estudante"] = input("Digite o nome do estudante: ")  # Solicita ao usuário o nome do estudante
        novo_registro["turma"] = input("Digite o código da turma: ")  # Solicita ao usuário o código da turma
        novo_registro["status"] = input("Digite o status da matrícula: ")  # Solicita ao usuário o status da matrícula

    registros.append(novo_registro)  # Adiciona o novo registro à lista de registros
    dados[chave] = registros  # Atualiza os registros da chave especificada nos dados
    salvar_dados(dados)  # Chama a função salvar_dados para salvar as alterações nos dados
    print("Registro incluído com sucesso.")  # Exibe uma mensagem informando que o registro foi incluído com sucesso