from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
gener = str(input('Qual seu genero: '))
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18 and gener == 'masculino':
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and gener == 'masculino':
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento!',format(saldo))
    ano = atual + saldo
    print('Seu Alistamento será em {}'.format(ano))
elif idade > 18 and gener == 'masculino':
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Você é do genero {} e não precisa se alistar.'.format(gener))