soma_pares = 0
cont = 0



for c in range(1, 7):
        numero = int(input('Digite o {} valor : '.format(c)))
        if numero % 2 == 0:
            soma_pares += numero
            cont += 1
        else:
            print('Você digitou o número {} e é impar, então ele não entrará na soma!'.format(numero))
print('Você informou o {} números PARES e a soma foi {}'.format(cont, soma_pares))