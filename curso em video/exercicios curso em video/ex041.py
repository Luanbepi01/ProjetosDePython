from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print(' o atleta tem {} anos de idade, e é da categoria mirim.'.format(idade))
elif idade <= 14:
    print(' o atleta tem {} anos de idade, e é da categoria infantil.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos de idade, e é da categoria junior.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos de idade, e é da categoria senior.'.format(idade))
else:
    print('O atleta tem {} anos de idade, e é da categoria master.'.format(idade))
