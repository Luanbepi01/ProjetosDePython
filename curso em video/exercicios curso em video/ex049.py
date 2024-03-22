from time import sleep
n1 = int(input('Digite um numero para ver a tabuada: '))
print('PROCESSANDO....')
print('-=' *14)
print('Tabuada do numero {}'.format(n1))
sleep(3)
for c in range(1, 11):
    resultado = n1 * c
    sleep(1.5)
    print('-=' * 14)
    print('PROCESSANDO....')
    print('{} x {} = {}'.format(n1, c, resultado))
