'''import random
from time import sleep

print('========== Bem vindo ao jogo de advinhação. Meu nome é computador! ==========')
print('Pensei em um número entre 0 e 10. Tente advinhar!')

numero_pensado = random.randint(0, 10)
tentativas = 0

while True:
    palpite = input('Digite seu palpite: ')

    print('PROCESSANDO...')
    sleep(2)

    if palpite.isdigit() and 0 <= int(palpite) <= 10:
        palpite = int(palpite)
        tentativas += 1
        if palpite == numero_pensado:
            print('Parabéns! Você acertou em {} tentativas(s).'.format(tentativas))
            break
        elif palpite < numero_pensado:
            print('Tente um número maior.')
        else:
            print('Tente um número menor,')
    else:
        print('Entrada inválida. por favor, digite um numero inteiro entre 0 e 10.')'''


from random import randint
computador = randint(0, 10)
print('Sou seu comnputador... Acabei de pensar em um número entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi?: ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu paplpite?: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas! Parabéns!'.format(palpite))
