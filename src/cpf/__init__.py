def validar_1digito(cpf):
    multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    resultados = []
    for c in range(len(cpf)):
        if c >= 9:
            break
        resultado = int(cpf[c]) * multiplicadores[c]
        resultados.append(resultado)
    soma = sum(resultados)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if int(cpf[9]) == resto:
        return resto
    else:
        raise ValueError("CPF INVALIDO")


def validar_2digito(cpf):
    validar_1digito(cpf)
    multiplicadores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    resultados = []
    for c in range(len(cpf)):
        if c >= 10:
            break
        resultado = int(cpf[c]) * multiplicadores[c]
        resultados.append(resultado)
    soma = sum(resultados)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if int(cpf[10]) == resto:
        return resto
    else:
        raise ValueError("CPF INVALIDO")


def validar_cpf(cpf):
    """
    Essa função retorna a validção do CPF
    :param cpf: CPF informado pelo usuário, pode conter infens ou pontos
    :type cpf: str
    :return:
    """
    cpf.replace('.', '')
    cpf.replace('-', '')
    if len(cpf) == 11:
        primeiro_digito = validar_1digito(cpf)
        if primeiro_digito != int(cpf[9]):
            raise ValueError('CPF INVALIDO')
        segundo_digito = validar_2digito(cpf)
        if segundo_digito != int(cpf[10]):
            raise ValueError('CPF INVALIDO')
    else:
        raise ValueError('CPF INVALIDO')

    return cpf
