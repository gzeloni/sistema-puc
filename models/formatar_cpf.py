def formatar_cpf(cpf):
    try:
        if len(cpf) != 11:
            raise ValueError("O CPF deve ter 11 dígitos.")

        cpf_formatado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        return cpf_formatado

    except ValueError as ve:
        print("Erro ao formatar CPF:", ve)
        return None
    except Exception as e:
        print("Ocorreu um erro ao formatar o CPF:", e)
        return None
