from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair''')
    opcao = int(input('>>>>>>> Qual sua opção? '))
    if opcao ==1:
        soma = n1 + n2
        print('A soma de {} + {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida! Tente novamente!')
    sleep(2)
    print('-=-' * 10)
print('Fim do programa! Volte Sempre!')
