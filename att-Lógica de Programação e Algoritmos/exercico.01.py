while True:
    inicio = int(input('Inserir dados? [0] - Não | [1] - Sim '))

    if inicio == 0:
        print('Fim do programa')
        break

    if inicio == 1:
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
        else:
            print('O Aluno(a) {} tirou {} e se enquadra no Conceito A'.format(nome_aluno, nota_final))

    else:
        print('Opção Inválida')