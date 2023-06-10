def listar_registros(chave, dados):
    try:
        # Acessa a lista de registros correspondente à chave especificada nos dados
        registros = dados[chave]

        if not registros:
            # Se a lista de registros estiver vazia, exibe uma mensagem indicando que não há registros
            print("\n\nNão há registros\n\n")

        else:
            for registro in registros:
                # Itera sobre cada registro na lista e imprime o registro
                print(registro)

    # Captura uma exceção KeyError que ocorre se a chave especificada não existir nos dados
    except KeyError:
        # Imprime uma mensagem indicando que a chave não foi encontrada
        print(f"A chave '{chave}' não foi encontrada nos dados.")

    # Captura qualquer outra exceção que ocorrer durante a listagem dos registros
    except Exception as e:
        # Imprime uma mensagem de erro genérica junto com a descrição da exceção ocorrida
        print("Ocorreu um erro durante a listagem dos registros:", e)
