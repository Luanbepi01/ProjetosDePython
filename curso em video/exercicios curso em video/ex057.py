'''while True:
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        print('Sexo registrado com sucesso voce escolheu o sexo: {}!'.format(sexo))
        break
    else:
        print('Sexo incorreto. Tente novamente com as poções [M/F]: ')'''

# correção do curso em video metodo mais simples

from time import sleep

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
print('PROCESSANDO....')
sleep(2)

while sexo not in 'MF':
    sexo = str(input('Dados inválido. Por favor, informe seu sexo: ')).strip().upper()[0]
    print('PROCESSANDO....')
    sleep(2)
print('Sexo {} REGISTRADO!!!'.format(sexo))
