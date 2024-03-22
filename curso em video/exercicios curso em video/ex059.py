'''while True:
    print('====== Menu ======')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do programa')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        resultado = num1 + num2
        print('A soma de {} e {} é {}'.format(num1, num2, resultado))

    elif opcao == 2:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        resultado = num1 * num2
        print('A multiplicação de {} e {} é {}'.format(num1, num2, resultado))

    elif opcao == 3:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        resultado = max(num1, num2)
        print('O maior numero entre {} e {} é {}'.format(num1, num2, resultado))

    elif opcao == 4:
        continue # Retorna ao inicio do loop para digitar novos numeros

    elif opcao == 5:
        print('Programa encerrado')
        break # sai do loop e encerra o programa

    else:
        print('Opção inválida. Tente novamente.')'''

#Revisao da atividade 59:


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:

    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>>>>>Qual  é a sua opção?: '))
    if  opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n1, soma))
    elif opção  == 2:
        mult = n1 * n2
        print('A multiplicação entre {} X {} é {}'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(' entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')