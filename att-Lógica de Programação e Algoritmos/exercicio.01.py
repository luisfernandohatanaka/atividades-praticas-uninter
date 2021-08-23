def ler_numero(mensagem):
    while True:
        try:
            f = float(input(mensagem))
            return f
        except ValueError:
            print('Digite um número válido')


def nome(msg):
    while True:
        nome_aluno = str(input('Nome do Aluno: '))
        if not nome_aluno.isalpha():
            print('Digite os valores corretos')
        else:
            return nome_aluno


def lista():
    print('|     Nota    |', '|   Conceito   |')
    print('|  0,0 a 2,9  |', '|      E       |')
    print('|  3,0 a 4,9  |', '|      D       |')
    print('|  5,0 a 6,9  |', '|      C       |')
    print('|  7,0 a 8,9  |', '|      B       |')
    print('|  9,0 a 10,0 |', '|      A       |')
    print('\n', ' ' * 6, 'Fim do programa!!')


while True:
    inicio = str(input('Inserir dados? [S/N]: ')).strip().upper()
    if inicio in 'N':
        break

    if inicio in 'S':
        nome_aluno = nome('Digite seu nome: ')
        nota_final = ler_numero('Nota final: ')

        if nota_final < 3:
            print('O Aluno(a) {} tirou {} e se enquadra no Conceito E'.format(nome_aluno, nota_final))
        elif nota_final < 5:
            print('O Aluno(a) {} tirou {} e se enquadra no Conceito D'.format(nome_aluno, nota_final))
        elif nota_final < 7:
            print('O Aluno(a) {} tirou {} e se enquadra no Conceito C'.format(nome_aluno, nota_final))
        elif nota_final < 9:
            print('O Aluno(a) {} tirou {} e se enquadra no Conceito B'.format(nome_aluno, nota_final))
        elif nota_final <= 10:
            print('O Aluno(a) {} tirou {} e se enquadra no Conceito A'.format(nome_aluno, nota_final))
        else:
            while nota_final > 10:
                print('Digite uma nota válida')
                nota_final = float(input('Nota final: '))
                if nota_final < 3:
                    print('O Aluno(a) {} tirou {} e se enquadra no Conceito E'.format(nome_aluno, nota_final))
                elif nota_final < 5:
                    print('O Aluno(a) {} tirou {} e se enquadra no Conceito D'.format(nome_aluno, nota_final))
                elif nota_final < 7:
                    print('O Aluno(a) {} tirou {} e se enquadra no Conceito C'.format(nome_aluno, nota_final))
                elif nota_final < 9:
                    print('O Aluno(a) {} tirou {} e se enquadra no Conceito B'.format(nome_aluno, nota_final))
                elif nota_final <= 10:
                    print('O Aluno(a) {} tirou {} e se enquadra no Conceito A'.format(nome_aluno, nota_final))
    else:
        print('Opção Inválida')
lista()
