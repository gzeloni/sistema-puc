from models.carregar_dados import carregar_dados
from models.menu import menu_operacoes
from models.trim_string import trim_string

def main():
    try:
        dados = carregar_dados()
        
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1. Estudantes")
            print("2. Disciplinas")
            print("3. Professores")
            print("4. Turmas")
            print("5. Matrículas")
            print("0. Sair")

            opcao_principal = trim_string(input("Escolha uma opção: "))

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
    
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)

    print("Fim da aplicação.")

if __name__ == "__main__":
    main()
