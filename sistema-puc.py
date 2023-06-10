from models.carregar_dados import carregar_dados  # Importa a função carregar_dados do módulo models.carregar_dados
from models.menu import menu_operacoes  # Importa a função menu_operacoes do módulo models.menu

def main():
    dados = carregar_dados()  # Chama a função carregar_dados e atribui o resultado à variável dados
    
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Estudantes")
        print("2. Disciplinas")
        print("3. Professores")
        print("4. Turmas")
        print("5. Matrículas")
        print("0. Sair")

        opcao_principal = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu

        if opcao_principal == "1":  # Se a opção escolhida for "1"
            menu_operacoes("estudantes", dados)  # Chama a função menu_operacoes passando a opção "estudantes" e os dados
        elif opcao_principal == "2":  # Se a opção escolhida for "2"
            menu_operacoes("disciplinas", dados)  # Chama a função menu_operacoes passando a opção "disciplinas" e os dados
        elif opcao_principal == "3":  # Se a opção escolhida for "3"
            menu_operacoes("professores", dados)  # Chama a função menu_operacoes passando a opção "professores" e os dados
        elif opcao_principal == "4":  # Se a opção escolhida for "4"
            menu_operacoes("turmas", dados)  # Chama a função menu_operacoes passando a opção "turmas" e os dados
        elif opcao_principal == "5":  # Se a opção escolhida for "5"
            menu_operacoes("matriculas", dados)  # Chama a função menu_operacoes passando a opção "matriculas" e os dados
        elif opcao_principal == "0":  # Se a opção escolhida for "0"
            break  # Sai do loop while True e encerra o programa
        else:  # Se a opção escolhida não for válida
            print("Opção inválida.")  # Exibe uma mensagem informando que a opção é inválida

    print("Fim da aplicação.")  # Exibe uma mensagem informando que a aplicação foi encerrada

if __name__ == "__main__":
    main()  # Chama a função main, que é o ponto de entrada do programa
