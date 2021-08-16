from operator import itemgetter


def ler_numero(mensagem):
    while True:
        try:
            f = int(input(mensagem))
            return f
        except ValueError:
            print('Digite um número válido')


lista = []
dicionario = {}

while True:
    print('Digite 0 [ZERO] no código para encerrar')
    dicionario['codigo'] = ler_numero('Código: ')
    if dicionario['codigo'] == 0:
        break
    else:
        dicionario['estoque'] = ler_numero('Estoque: ')
        dicionario['minimo'] = ler_numero('Mínimo: ')
        lista.append(dicionario.copy())
listaOrdenada = sorted(lista, key=itemgetter('codigo'))

print(listaOrdenada)
