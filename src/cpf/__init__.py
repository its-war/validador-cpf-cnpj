# def fatiamento_cpf():
# fatia_1 = cpf[:3]
# fatia_2 = cpf[3:6]
# fatia_3 = cpf[6:9]
# fatia_4 = cpf[9:]
# return (f'{fatia_1}.{fatia_2}.{fatia_3}-{fatia_4}')

def validar_1digito(cpf):
    multiplicadores = []  # olhe os multiplicadores no pdf que jarbas deu
    resultados = []  # inves de retornar os resultados, vc deve salvar dentro da lista e so no final vc soma e divide
    for c in range(len(cpf)):
        resultado = cpf[c] * c  # aqui vc substitui o segundo C pelo multiplicador certo
        print(f'Resultado {resultado}')
        return (resultado * 10) / 11
        # vc nao pode dar um return dentro do for,
        # a nao ser que queira parar o processo do for


def validar_2digito(cpf, primeiro_digito):
    # ESQUEÇA QUE EXISTE O SEGUNDO DIGITO
    # pra vc ele so existe quando vc fizer o primeiro
    for c in range(11, 2, -1):
        resultado = cpf * c
        print(f'Resultado {c}')
        return (resultado * 10) / 11


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
        # depois de pegar o primeiro digito, deve comparar no cpf, se está correto
        # depois deve jogar dentro da função do segundo digito
    else:
        raise ValueError('CPF INVALIDO')
