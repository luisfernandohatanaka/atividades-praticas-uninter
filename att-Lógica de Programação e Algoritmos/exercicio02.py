def email(n, s):
    res = (nome[0].lower() + sobrenome[:].lower() + '@algoritmos.com.br')
    return res


while True:
    nome = str(input('Digite seu nome: ')).strip().title()
    sobrenome = str(input('Digite seu sobrenome: ')).strip().title()
    if nome.isalpha() and sobrenome.isalpha():
        break
    else:
        print('[ERRO]. Digite apenas letras')
emailCompleto = email(nome, sobrenome)
print('Sr(a) {} {}, seu email é {}'.format(nome, sobrenome, emailCompleto))
