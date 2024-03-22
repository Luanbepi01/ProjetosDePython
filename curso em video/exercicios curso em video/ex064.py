num = 0
cont = 0
soma = 0
'''posso colocar as variaveis juntos exemplo abaixo
num = cont = soma = 0'''

while num != 999:
    num = int(input('Digite um valor: '))
    if num != 999:
        soma += num
        cont += 1

print('voce digitou {} valores e a soma entre eles foi {}'.format(cont, soma))