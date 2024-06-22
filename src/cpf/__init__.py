def validar_1digito(cpf):
    multiplicadores = [10,9,8,7,6,5,4,3,2]  # olhe os multiplicadores no pdf que jarbas deu
    resultados = []  # inves de retornar os resultados, vc deve salvar dentro da lista e so no final vc soma e divide  
    for c in range(len(cpf)):
        if c >= 9:
            break
        resultado = int(cpf[c]) * multiplicadores[c]  # aqui vc substitui o segundo C pelo multiplicador certo
        resultados.append(resultado)
    soma = sum(resultados)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if int(cpf[9]) == resto:
        return resto
    else:
        return False
        # vc nao pode dar um return dentro do for,
        # a nao ser que queira parar o processo do for


def validar_2digito(cpf):
    # ESQUEÇA QUE EXISTE O SEGUNDO DIGITO
    # pra vc ele so existe quando vc fizer o primeiro
    validar_1digito(cpf)
    multiplicadores = [11,10,9,8,7,6,5,4,3,2]
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
        return False
    
    

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
    

t = input('cpf: ')
print(validar_1digito(t))
print(validar_2digito(t))
52998224725