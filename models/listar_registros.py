def listar_registros(chave, dados):
    registros = dados[chave]  # Obtém a lista de registros da chave especificada nos dados
    for registro in registros:  # Itera sobre cada registro na lista de registros
        print(registro)  # Imprime o registro