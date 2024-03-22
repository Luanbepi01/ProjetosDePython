primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
term = primeiro_termo
cont = 1
total = 0
mais = 10
print('Os 10 primeiros termos da PA são: ')
print('-=' * 10)
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(term), end='')
        term += razao
        cont += 1
    print('PAUSA...')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Progressao finalizada com {} termos mostrados!'.format(total))