'''print('=' *50)
print('CADASTRE UM PRODUTO'.center(50))
print('=' *50)

idade = 0
sexo = 0
cont = 0
maior_idade = 0
mulher_menor = 0

opção = 'S'

while opção == 'S':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    opção = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    print('=' *50)
    if sexo == 'M':
        cont += 1
    elif sexo == 'F' and idade < 20:
        mulher_menor += 1
    if idade > 18:
        maior_idade += 1


print(f'Foram cadastrada   {cont} pessoas do sexo masculino. ')
print(f'Foram cadastradas {maior_idade} pessoas maiores de 18 anos. ')
print(f'Foram cadastradas {mulher_menor} mulheres com menos de 20 anos')'''

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais  de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
print('Acabou!')