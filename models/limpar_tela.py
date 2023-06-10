import os


def limpar_tela():
    try:
        # Verifica o sistema operacional atual e usa o comando apropriado para limpar a tela do console
        # 'cls' é usado no Windows e 'clear' é usado em sistemas Unix-like (Linux, macOS)
        os.system('cls' if os.name == 'nt' else 'clear')

    # Captura qualquer exceção ocorrida durante a limpeza da tela
    except Exception as e:
        # Imprime uma mensagem de erro genérica junto com a descrição da exceção ocorrida
        print("Ocorreu um erro ao limpar a tela:", e)
