# A função validar_codigo recebe um código, uma chave e um dicionário de dados como argumentos
# Ela verifica se o código existe nos registros correspondentes à chave fornecida no dicionário de dados
def validar_codigo(codigo, chave, dados):
    registros = dados.get(chave, [])
    # Percorre cada registro na lista de registros correspondente à chave
    for registro in registros:
        # Compara o código do registro atual com o código fornecido
        # Se forem iguais, significa que o código existe nos registros
        if registro["codigo"] == codigo:
            # Retorna True para indicar que o código é válido e existe nos registros
            return True

    # Se o loop terminar sem encontrar um registro com o código fornecido, retorna False para indicar que o código é inválido ou não existe nos registros
    return False
