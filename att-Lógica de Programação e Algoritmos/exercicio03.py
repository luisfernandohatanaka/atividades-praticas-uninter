import random
from time import sleep

sorteio = list()

while True:
    nome = str(input('Nome do doador: ')).strip().title()
    valor_doado = int(input('Digite o valor doado: '))
    total, resto = divmod(valor_doado, 10)

    if resto == 0:
        sorteio.extend([nome] * total)
    else:
        print('valor inválido, deve ser múltiplo de 10 e maior que zero(10, 20, 30...')

    continuar = str(input('Deseja continuar?: [S/N] ')).upper()[0]
    if continuar in 'S':
        continue
    elif continuar in 'N':
        break

print(f'A lista de doadores ficou assim: {sorteio}')
print('Sorteando!!!')

for cont in range (5,0,-1):
    print('{}{}{}'.format('\033[1;31m', cont, '\033[m'))
    sleep(1)
    random.shuffle(sorteio)

ganhador = random.choice(sorteio)
print(f'O ganhador(a) foi {ganhador}')

