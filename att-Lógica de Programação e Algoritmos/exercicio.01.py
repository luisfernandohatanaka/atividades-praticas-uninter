while True:
    inicio = str(input('Inserir dados? [S/N]: ')).strip().upper()

    if inicio in 'N NAO':
        print('Fim do programa')
        break

    if inicio in 'S SIM':
        nome_aluno = str(input('Nome do Aluno: '))
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