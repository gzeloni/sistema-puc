def listar_registros(chave, dados):
    registros = dados[chave]  # Obtém a lista de registros da chave especificada nos dados
    
    if not registros:  # Verifica se a lista de registros está vazia
        print("\n\nNão há estudantes cadastrados\n\n")
    else:
        for registro in registros:  # Itera sobre cada registro na lista de registros
            print(registro)  # Imprime o registro