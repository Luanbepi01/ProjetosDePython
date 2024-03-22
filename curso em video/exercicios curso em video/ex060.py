'''from time import sleep
num = int(input('Digite um numero para calcular o fatorial: '))
print('CALCULANDO....')
sleep(2)

if num < 0:
    print('Por favor, digite um numero não negativo. ')
else:
    fatorial = 1
    i = 1
    while i <= num:
        fatorial *= i
        i += 1
        print('{} = {}'.format(num, fatorial))'''

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{} '.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
