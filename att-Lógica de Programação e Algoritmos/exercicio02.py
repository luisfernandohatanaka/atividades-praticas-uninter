# function que pega dois parametros (nome e sobrenome)
# uma variavel dentro da function que pega somente a a primeira letra do nome e o sobrenome completo, converte tudo para minusculo(lower) e concatena com @algoritmos... retornando uma res
def email(n, s):
    res = (nome[0].lower() + sobrenome[:].lower() + '@algoritmos.com.br')
    return res

# fiz uma validação nesse while. aceitando somente "letras".
# adicionado 2 metodos ao final, um para tirar os espaços no inicio e final do input, e outro para deixa a primeira palavra do input sempre em Capslock
while True:
    nome = str(input('Digite seu nome: ')).strip().title()
    sobrenome = str(input('Digite seu sobrenome: ')).strip().title()
    if nome.isalpha() and sobrenome.isalpha():
        break
    # caso seja digitado numeros, 2 ou + nomes, ou qualquer caracter especial, ele cai no else e volta para o looping
    else:
        print('[ERRO]. Digite apenas letras')
# variavel criada para criar o email
emailCompleto = email(nome, sobrenome)
#  print na tela com o email e o nome da pessoa
print('Sr(a) {} {}, seu email é {}'.format(nome, sobrenome, emailCompleto))
