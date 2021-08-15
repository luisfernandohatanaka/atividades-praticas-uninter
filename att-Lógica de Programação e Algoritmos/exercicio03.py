import random

sorteio = list()

while True:
    nome = str(input('Nome do doador: '))
    valor_doado = int(input('Digite o valor doado: '))
    total, resto = divmod(valor_doado, 10)

    if resto == 0:
        sorteio.extend([nome] * total)
    else:
        print('valor inválido, deve ser múltiplo de 10 e maior que zero')

    continuar = str(input('Deseja continuar?: [S/N] '))
    if continuar in 'Ss':
        continue
    else:
        break

print(sorteio)
random.shuffle(sorteio)
ganhador = random.choice(sorteio)
print(ganhador)

