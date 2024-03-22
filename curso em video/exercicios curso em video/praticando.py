'''import time
num = 1



while num != 0:
    num = int(input('Digite um numero: '))
    print('PROCESSANDO...')
    time.sleep(2)
    if num % 2 == 0:
        print('O numero digitado é PAR!')
    else:
        print('O numero digitado é IMPAR!')
print('FIM do programa!')'''

'''escolh = str(input('Escolha qual lado voce quer ir: '))

if escolh == 'direita':
    print('voce escolheu o lado {} e achou um dinheiro!'.format(escolh))
elif escolh == 'esquerda':
    print('voce escolheu o lado {} e achou uma bolsa nova!'.format(escolh))
else:
    print('voce escolheu a opção invalida, tente novamente!')'''

'''import time

def contador(segundos):
    for i in range(segundos, 0, -1):
        min, seg = divmod(i, 60)
        texto = f"{min:02d}:{seg:02d}"
        print(texto)
        time.sleep(1)

    print("Contagem regressiva concluída!")

contador(10)'''

import time
num = 0

while num  < 11:
    print(num)
    num += 1
    time.sleep(1)
print('Fim da contagem!!')
