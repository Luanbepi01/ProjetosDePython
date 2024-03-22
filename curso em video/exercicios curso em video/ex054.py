from datetime import date
from time import sleep

ano_atual = date.today().year

maiores_idade = 0
menores_idade = 0

for c in range(1, 8):
    print('-=' * 45)
    ano_nascimento = int(input('Digite o ano de nascimento da pessoa {}°: '.format(c)))

    idade = ano_atual - ano_nascimento

    if idade >= 21:
        maiores_idade += 1
    else:
        menores_idade += 1
print('-=' * 45)
print('PROCESSANDO....')
sleep(3)
print('-=' * 45)
print('Resultado: {} pessoas são maiores de idade.'.format(maiores_idade))
print('{} pessoas ainda não atingiram a maioridade.'.format(menores_idade))
print('-=' * 45)