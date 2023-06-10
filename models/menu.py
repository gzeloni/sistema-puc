from models.atualizar_registro import atualizar_registro
from models.excluir_registro import excluir_registro
from models.incluir_registro import incluir_registro
from models.limpar_tela import limpar_tela
from models.listar_registros import listar_registros
from models.trim_string import trim_string


def menu_operacoes(chave, dados, codigo):
    limpar_tela()
    while True:
        try:
            print("\n===== MENU DE OPERAÇÕES =====")
            print("1. Incluir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar ao menu principal")

            opcao_operacoes = trim_string(input("Escolha uma operação: "))

            # Se a opção selecionada for "1", chama a função incluir_registro passando a chave e os dados
            if opcao_operacoes == "1":
                incluir_registro(chave, dados)
            # Se a opção selecionada for "2", chama a função listar_registros passando a chave e os dados
            elif opcao_operacoes == "2":
                listar_registros(chave, dados)
            # Se a opção selecionada for "3", chama a função atualizar_registro passando a chave e os dados
            elif opcao_operacoes == "3":
                atualizar_registro(chave, dados)
            # Se a opção selecionada for "4", chama a função excluir_registro passando a chave, os dados e o código
            elif opcao_operacoes == "4":
                excluir_registro(chave, dados, codigo)
            # Se a opção selecionada for "0", interrompe o loop e retorna ao menu principal
            elif opcao_operacoes == "0":
                break
            # Se a opção selecionada não corresponder a nenhuma das opções disponíveis, exibe uma mensagem de opção inválida
            else:
                print("Opção inválida.")

        # Captura qualquer exceção que ocorrer durante a execução das operações do menu
        except Exception as e:

            # Exibe uma mensagem de erro genérica junto com a descrição da exceção ocorrida
            print("Ocorreu um erro durante a execução da operação:", e)
