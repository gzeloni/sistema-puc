from models.atualizar_registro import atualizar_registro  # Importa a função atualizar_registro do módulo models.atualizar_registro
from models.excluir_registro import excluir_registro  # Importa a função excluir_registro do módulo models.excluir_registro
from models.incluir_registro import incluir_registro  # Importa a função incluir_registro do módulo models.incluir_registro
from models.listar_registros import listar_registros  # Importa a função listar_registros do módulo models.listar_registros

def menu_operacoes(chave, dados):
    while True:
        print("\n===== MENU DE OPERAÇÕES =====")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("0. Voltar ao menu principal")

        opcao_operacoes = input("Escolha uma operação: ")  # Solicita ao usuário a escolha de uma operação

        if opcao_operacoes == "1":  # Se a opção for "1"
            incluir_registro(chave, dados)  # Chama a função incluir_registro passando a chave e os dados como argumentos
        elif opcao_operacoes == "2":  # Se a opção for "2"
            listar_registros(chave, dados)  # Chama a função listar_registros passando a chave e os dados como argumentos
        elif opcao_operacoes == "3":  # Se a opção for "3"
            atualizar_registro(chave, dados)  # Chama a função atualizar_registro passando a chave e os dados como argumentos
        elif opcao_operacoes == "4":  # Se a opção for "4"
            excluir_registro(chave, dados)  # Chama a função excluir_registro passando a chave e os dados como argumentos
        elif opcao_operacoes == "0":  # Se a opção for "0"
            break  # Encerra o loop e volta ao menu principal
        else:
            print("Opção inválida.")  # Exibe uma mensagem informando que a opção é inválida