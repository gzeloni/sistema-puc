from models.atualizar_registro import atualizar_registro
from models.excluir_registro import excluir_registro
from models.incluir_registro import incluir_registro
from models.listar_registros import listar_registros
from models.trim_string import trim_string

def menu_operacoes(chave, dados):
    while True:
        try:
            print("\n===== MENU DE OPERAÇÕES =====")
            print("1. Incluir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar ao menu principal")

            opcao_operacoes = trim_string(input("Escolha uma operação: "))

            if opcao_operacoes == "1":
                incluir_registro(chave, dados)
            elif opcao_operacoes == "2":
                listar_registros(chave, dados)
            elif opcao_operacoes == "3":
                atualizar_registro(chave, dados)
            elif opcao_operacoes == "4":
                excluir_registro(chave, dados)
            elif opcao_operacoes == "0":
                break
            else:
                print("Opção inválida.")
        
        except Exception as e:
            print("Ocorreu um erro durante a execução da operação:", e)
