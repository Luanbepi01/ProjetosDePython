num = cont = soma = media = 0

while num >= 0:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    soma = soma + num
    cont += 1
    media = soma /cont
print(f'Você digitou {cont}, e a média dos numeros digitados foi {media}')
print('Acabou....')