primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
term = primeiro_termo
cont = 1


print('Os 10 primeiros termos da PA são: ')
while cont <= 10:
    print('{} -> '.format(term), end='')
    term += razao
    cont += 1
print('FIM....')