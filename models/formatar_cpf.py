# Função para formatar um CPF
def formatar_cpf(cpf):
    try:
        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            raise ValueError("O CPF deve ter 11 dígitos.")

        # Formata o CPF com pontos e traço
        cpf_formatado = "{}.{}.{}-{}".format(cpf[:3],
                                             cpf[3:6], cpf[6:9], cpf[9:])
        return cpf_formatado

    # Trata a exceção se o CPF não tiver 11 dígitos
    except ValueError as ve:
        print("Erro ao formatar CPF:", ve)
        return None
    # Trata outras exceções que possam ocorrer durante a formatação do CPF
    except Exception as e:
        print("Ocorreu um erro ao formatar o CPF:", e)
        return None
