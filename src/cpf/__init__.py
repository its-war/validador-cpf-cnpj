def cpf_valido():
    if len(cpf) == 11:
        validar_1digito()
    else:
        return False

# def fatiamento_cpf():
    # fatia_1 = cpf[:3]
    # fatia_2 = cpf[3:6]
    # fatia_3 = cpf[6:9]
    # fatia_4 = cpf[9:]
    # return (f'{fatia_1}.{fatia_2}.{fatia_3}-{fatia_4}')
    
def validar_1digito():
    for c in range(10, 2, -1):
        resultado = cpf * c
        print(f'Resultado {resultado}')
        resulta = (resultado * 10) / 11
    return resulta   

def validar_2digito():
    validar_1digito()
    for c in range(11, 2 , -1):
        resultado = cpf * c
        print(f'Resultado {c}')
        resulta = (resultado * 10) / 11
    return resulta
    
cpf = int(input('Digite cpf: '))
print(validar_1digito())

    