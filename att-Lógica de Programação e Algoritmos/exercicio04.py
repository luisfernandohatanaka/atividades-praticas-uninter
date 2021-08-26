# do modulo operator foi importado a função itemgetter
from operator import itemgetter

# validação de numeros
def ler_numero(mensagem):
    while True:
        try:
            f = int(input(mensagem))
            return f
        except ValueError:
            print('Digite um número válido')

# criação de lista e dicionário
lista = []
dicionario = {}

# laço de repetição
while True:
    # se o código for ==  0 ele encerra o programa
    print('Digite 0 [ZERO] no código para encerrar')
    dicionario['codigo'] = ler_numero('Código: ')
    if dicionario['codigo'] == 0:
        break
    else:
        dicionario['estoque'] = ler_numero('Estoque: ')
        dicionario['minimo'] = ler_numero('Mínimo: ')
        # depois de ler os 3 valores, ele adiciona uma copia do dicionario numa lista vazia
        lista.append(dicionario.copy())
# utilizado sorted para deixar a lista em ordem crescente referente a key 'codigo'.
listaOrdenada = sorted(lista, key=itemgetter('codigo'))

# print final da lista ordenada pelo código
print(listaOrdenada)