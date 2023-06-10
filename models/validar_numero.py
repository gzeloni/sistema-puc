import re

def validar_numero(entrada):
    padrao = r'^\d+$'  # Regex para verificar se a string é composta apenas por dígitos
    return re.match(padrao, entrada) is not None