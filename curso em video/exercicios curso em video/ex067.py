'''# programa de tabuada!!
num = 0
cont = 0
soma = 0

while True:
    num  = int(input('Digite um numero para ver sua tabuada(aperte um numero negativo para Encerrar o programa): '))
    if num < 0:
        break
    print('=' * 16)

    for cont in range(1, 11):
        soma = num * cont
        print(f' {num} x {cont} = {soma}')
    print('=' *16)
print('Acabou...')'''

while True:
    num = int(input('Digite um número para ver a sua tabuada (aperte um numero negativo para encerrar o programa.): '))
    if num < 0:
        break
    print('=' *50)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('=' *50)
print(input('PROGRAMA TABUADA ENCERRADA. Volte sempre!'))