'''n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''

'''nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')'''

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome:-^20} tem  {idade} anos e ganha R${salario:.2f}')