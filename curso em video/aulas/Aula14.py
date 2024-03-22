#Aula  14 sobre Estrutura de repetição while!

'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''


# Enquanto o numero for diferente!
#observação: while tem que ter uma variavel começando com 1 ou outro numero.
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

#Lendo uma resposta.
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')'''

# Vendo de um numero é par ou impar!
'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))'''