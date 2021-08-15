def email(n, s):
    res = (nome[0].lower() + sobrenome[:].lower() + '@algoritmos.com.br')
    return res


nome = input('Digite seu nome: ').strip().title()
sobrenome = input('Digite seu sobrenome: ').strip().title()
x = email(nome, sobrenome)
print('Sr(a) {} {}, seu email é {}'.format(nome, sobrenome, x))