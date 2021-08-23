# importado modulo random
# do modulo time foi importado a função sleep
import random
from time import sleep

# funçao para validar somente numeros
def ler_numero(mensagem):
    while True:
        try:
            f = int(input(mensagem))
            return f
        except ValueError:
            print('Digite um número válido')

# lista de sorteio vazia
sorteio = list()

print('Doar somente valores multiplos de 10.')
# inicio do looping
while True:
    # outro looping para validar um nome
    while True:
        nome = str(input('Nome do doador: ')).strip().title()
        if nome.isalpha():
            break
        else:
            print('Digite um nome válido')
    valor_doado = ler_numero('Digite o valor doado: ')
    # variavel utilizando a funçao divmod (receber o quociente de valor_dado / por 10)
    total, resto = divmod(valor_doado, 10)
    # se o quociente for 0 ele é verdadeiro e cai nessa condição
    # o nome do doador é adicionado na lista + o tanto de vezes que ele doou valores multiplos de 10
    if resto == 0:
        sorteio.extend([nome] * total)
    # se for digitado valores != de multiplos de 10, ele cai nesse else, caindo num looping até digitar o valor correto.
    else:
        while True:
            print('valor inválido, deve ser múltiplo de 10 e maior que zero(10, 20, 30...')
            valor_doado = ler_numero('Digite o valor doado: ')
            total, resto = divmod(valor_doado, 10)
            # se for digitado o valor correto ele sai do looping
            if resto == 0:
                sorteio.extend([nome] * total)
                break
    # input para verificar se ainda a pessoa deseja colocar os dados
    continuar = str(input('Deseja continuar?: [S/N] ')).upper()[0]
    # se o continuar nao for N ou S ele vai continuar no looping
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?: [S/N] ')).upper()[0]
    # se o continuar for == N ele vai quebrar o looping
    if continuar in 'N':
        break

# depois de finalizado o looping, é printado no programa a lista de sorteio referente aos nomes e doações colocadas.
print(f'A lista de doadores ficou assim: {sorteio}')
print('Sorteando!!!')

# fiz uma contagem regressiva utilizando for e o sleep importado do time(para fins visuais do codigo)
for cont in range(5, 0, -1):
    print('{}{}{}'.format('\033[1;31m', cont, '\033[m'))
    sleep(1)
    # a cada ciclo do for, a lista é embaralhada com shuffle
    random.shuffle(sorteio)

# ganhador sera definido com uma escolha aleatório na lista usando o random.choice
ganhador = random.choice(sorteio)
# print final com o nome do ganhador
print(f'PARABÉNS {ganhador}, voce ganhou o sorteio')
