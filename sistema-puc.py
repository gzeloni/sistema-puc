from models.carregar_dados import carregar_dados
from models.menu import menu_operacoes

def main():
    global dados
    dados = carregar_dados()
    
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Estudantes")
        print("2. Disciplinas")
        print("3. Professores")
        print("4. Turmas")
        print("5. Matrículas")
        print("0. Sair")

        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == "1":
            menu_operacoes("estudantes", dados)
        elif opcao_principal == "2":
            menu_operacoes("disciplinas", dados)
        elif opcao_principal == "3":
            menu_operacoes("professores", dados)
        elif opcao_principal == "4":
            menu_operacoes("turmas", dados)
        elif opcao_principal == "5":
            menu_operacoes("matriculas", dados)
        elif opcao_principal == "0":
            break
        else:
            print("Opção inválida.")

    print("Fim da aplicação.")

if __name__ == "__main__":
    main()
