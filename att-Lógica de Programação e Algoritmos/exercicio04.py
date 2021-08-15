from operator import itemgetter

lista = []
dicionario = {}

while True:
    dicionario['codigo'] = int(input('Informe o código. Digite 0 [ZERO] para encerrar: '))
    if dicionario['codigo'] == 0:
        break
    else:
        dicionario['estoque'] = int(input('Informe o valor: '))
        dicionario['minimo'] = int(input('Informe o valor: '))
        lista.append(dicionario.copy())
listaOrdenada = sorted(lista, key=itemgetter('codigo'))

print(listaOrdenada)