from operator import itemgetter

lista = []
dicionario = {}

while True:
    print('Digite 0 [ZERO] no código para encerrar')
    dicionario['codigo'] = int(input('Código: '))
    if dicionario['codigo'] == 0:
        break
    else:
        dicionario['estoque'] = int(input('Estoque: '))
        dicionario['minimo'] = int(input('Mínimo: '))
        lista.append(dicionario.copy())
listaOrdenada = sorted(lista, key=itemgetter('codigo'))

print(listaOrdenada)