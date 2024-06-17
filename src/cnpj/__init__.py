def __validar_primeiro_digito(cnpj):
    multiplicador = 5
    resultados = []

    for i in range(len(cnpj)):
        if i > 11:
            break

        resultados.append(int(cnpj[i]) * multiplicador)

        if multiplicador != 2:
            multiplicador -= 1
        else:
            multiplicador = 9

    primeiro_digito = sum(resultados) % 11
    if primeiro_digito < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - primeiro_digito

    return primeiro_digito


def __validar_segundo_digito(cnpj, primeiro_digito):
    multiplicador = 6
    resultados = []
    for i in range(len(cnpj)):
        if i < 12:
            resultados.append(int(cnpj[i]) * multiplicador)
        elif i == 12:
            resultados.append(primeiro_digito * multiplicador)
        else:
            break

        if multiplicador != 2:
            multiplicador -= 1
        else:
            multiplicador = 9

    segundo_digito = sum(resultados) % 11
    if segundo_digito < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - segundo_digito
    return segundo_digito


def validar_cnpj(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('/', '')

    try:
        int(cnpj)
    except ValueError:
        raise ValueError('CNPJ inválido')

    if len(cnpj) != 14:
        raise ValueError('CNPJ inválido')

    primeiro_digito = __validar_primeiro_digito(cnpj)
    if primeiro_digito != int(cnpj[12]):
        raise ValueError('CNPJ inválido')

    segundo_digito = __validar_segundo_digito(cnpj, primeiro_digito)
    if segundo_digito != int(cnpj[13]):
        raise ValueError('CNPJ inválido')

    return cnpj
