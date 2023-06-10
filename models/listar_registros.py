def listar_registros(chave, dados):
    try:
        registros = dados[chave]

        if not registros:
            print("\n\nNão há estudantes cadastrados\n\n")
        else:
            for registro in registros:
                print(registro)

    except KeyError:
        print(f"A chave '{chave}' não foi encontrada nos dados.")
    except Exception as e:
        print("Ocorreu um erro durante a listagem dos registros:", e)
