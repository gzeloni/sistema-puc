# O código a seguir é um programa que exibe um menu principal e permite ao usuário escolher uma opção. 
# Dependendo da opção escolhida, o programa chama uma função específica para lidar com aquela opção.

# Importa as funções necessárias para o programa
from models.carregar_dados import carregar_dados
from models.limpar_tela import limpar_tela
from models.menu import menu_operacoes
from models.trim_string import trim_string

# Função principal do programa
def main():
    try:
        # Carrega os dados do arquivo
        dados = carregar_dados()
        
        # Loop principal do programa
        while True:
            # Limpa a tela do console
            limpar_tela()
            
            # Exibe o menu principal
            print("\n===== MENU PRINCIPAL =====")
            print("1. Estudantes")
            print("2. Disciplinas")
            print("3. Professores")
            print("4. Turmas")
            print("5. Matrículas")
            print("0. Sair")
            
            # Obtém a opção selecionada pelo usuário
            opcao_principal = trim_string(input("Escolha uma opção: "))

            # Verifica a opção selecionada e chama o menu correspondente
            if opcao_principal == "1":
                menu_operacoes("estudantes", dados, "codigo")
            elif opcao_principal == "2":
                menu_operacoes("disciplinas", dados, "codigo")
            elif opcao_principal == "3":
                menu_operacoes("professores", dados, "codigo")
            elif opcao_principal == "4":
                menu_operacoes("turmas", dados, "codigo")
            elif opcao_principal == "5":
                menu_operacoes("matriculas", dados, "codigo")
            elif opcao_principal == "0":
                # Sai do loop e encerra o programa
                break
            else:
                # Mensagem de opção inválida
                print("Opção inválida.")
    
    except FileNotFoundError:
        # Mensagem de erro quando o arquivo de dados não é encontrado
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        # Mensagem de erro genérico para outras exceções
        print("Ocorreu um erro:", e)

    # Mensagem exibida quando o programa é encerrado
    print("Fim da aplicação.")

# Executa a função principal se o arquivo for executado diretamente
if __name__ == "__main__":
    main()