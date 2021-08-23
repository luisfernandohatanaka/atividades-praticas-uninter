import random
from time import sleep


def ler_numero(mensagem):
    while True:
        try:
            f = int(input(mensagem))
            return f
        except ValueError:
            print('Digite um número válido')


sorteio = list()

print('Doar somente valores multiplos de 10.')
while True:
    while True:
        nome = str(input('Nome do doador: ')).strip().title()
        if nome.isalpha():
            break
        else:
            print('Digite um nome válido')
            continue
    valor_doado = ler_numero('Digite o valor doado: ')
    total, resto = divmod(valor_doado, 10)
    if resto == 0:
        sorteio.extend([nome] * total)
    else:
        while True:
            print('valor inválido, deve ser múltiplo de 10 e maior que zero(10, 20, 30...')
            valor_doado = ler_numero('Digite o valor doado: ')
            total, resto = divmod(valor_doado, 10)
            if resto == 0:
                sorteio.extend([nome] * total)
                break

    continuar = str(input('Deseja continuar?: [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?: [S/N] ')).upper()[0]
    if continuar in 'N':
        break

print(f'A lista de doadores ficou assim: {sorteio}')
print('Sorteando!!!')

for cont in range(5, 0, -1):
    print('{}{}{}'.format('\033[1;31m', cont, '\033[m'))
    sleep(1)
    random.shuffle(sorteio)

print(sorteio)
'''ganhador = random.choice(sorteio)
print(f'O ganhador(a) foi {ganhador}') '''
