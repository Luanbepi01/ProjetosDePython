numero = int(input('Digite um numero inteiro: '))

if numero > 1:
    for c in range(2, int(numero ** 0.5) + 1):
        if numero % c == 0:
            print('{} não é um número primo.'.format(numero))
            break
    else:
        print('{} é um número primo.'.format(numero))
else:
    print('{} não é um número primo.'.format(numero))
