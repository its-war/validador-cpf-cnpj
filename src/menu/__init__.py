from src import cnpj
from src import cpf
from time import sleep
import platform
import os


def limpar_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    cpfs_validados = 0
    cpfs_invalidados = 0

    cnpjs_validados = 0
    cnpjs_invalidados = 0

    while True:
        limpar_terminal()
        print('             MENU')
        print('1 — Validar CPF')
        print('2 — Validar CNPJ')
        print('3 — Sair')

        op = input('Digite a opção: ')

        if op == 'cpf' or op == '1':
            while True:
                limpar_terminal()
                cpf_text = input('Digite o CPF: ')
                try:
                    cpf.validar_cpf(cpf_text)
                except ValueError:
                    print('CPF INVALIDO')
                    print('Entre em contato com a receita federal.')
                    cpfs_invalidados += 1
                    sleep(3)
                else:
                    print('CPF VALIDO')
                    cpfs_validados += 1
                    break
        elif op == '2' or op == 'cnpj':
            while True:
                limpar_terminal()
                cnpj_text = input('Digite o CNPJ: ')
                try:
                    cnpj.validar_cnpj(cnpj_text)
                except ValueError:
                    print('CNPJ INVALIDO.')
                    print('Entre em contato com a receita federal.')
                    cnpjs_invalidados += 1
                    sleep(3)
                else:
                    print('CNPJ VALIDO')
                    cnpjs_validados += 1
                    break
        elif op == '3' or op == 'sair':
            print(f'CPFs validados: {cpfs_validados}')
            print(f'CPFs invalidados: {cpfs_invalidados}')
            print()
            print(f'CNPJs validados: {cnpjs_validados}')
            print(f'CNPJs invalidados: {cnpjs_invalidados}')
            print()
            print('Saindo em 5 segundos...')
            sleep(5)
            exit(0)
        else:
            print('Opcao Invalida')
        sleep(3)
