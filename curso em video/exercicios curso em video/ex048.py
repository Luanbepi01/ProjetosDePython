soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} numero impares multiplos de três no intervalo de 1 até 500 é {}:'.format(cont, soma))
