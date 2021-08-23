# Fiz uma function para validar numeros reais no input da nota
def ler_numero(msg):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print('Digite um número válido')

# Uma outra function para validar somente letras no input do nome
def nome(msg):
    while True:
        nome_aluno = str(input('Nome do Aluno: '))
        if not nome_aluno.isalpha():
            print('Digite os valores corretos')
        else:
            return nome_aluno

# Uma function para imprimir a tabela de nota e conceito
def lista():
    print('|     Nota    |', '|   Conceito   |')
    print('|  0,0 a 2,9  |', '|      E       |')
    print('|  3,0 a 4,9  |', '|      D       |')
    print('|  5,0 a 6,9  |', '|      C       |')
    print('|  7,0 a 8,9  |', '|      B       |')
    print('|  9,0 a 10,0 |', '|      A       |')
    print('\n', ' ' * 6, 'Fim do programa!!')

# Laço de repetição
while True:
    # Se meu input receber um "N" meu laço é quebrado e o programa é finalizado
    # Se ele receber qualquer outra letra, ele entra em looping. Somente a letra "N ou S" são aceitas nessa laço
    inicio = str(input('Inserir dados? [S/N]: ')).strip().upper()
    if inicio in 'N':
        break
    # Se ele receber um "S" ele entra nessa condição
    if inicio in 'S':
        # Aqui é feita a chamado pra nossa função (nome, ler_numero)
        nome_aluno = nome('Digite seu nome: ')
        nota_final = ler_numero('Nota final: ')
        # Aqui estão todas as condições referente a nota inserida na variavel nota_final
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
            # Se for inserido uma nota maior que 10, ele entra em outro looping. Somente inserindo uma nota <=10 ele sai do looping.
            while nota_final > 10:
                print('Digite uma nota válida [0 a 10]')
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
# No final do programa é impresso a lista de notas e conceitos, para a pessoa conferir se esta realmente certo.
lista()
