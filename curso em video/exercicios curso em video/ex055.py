maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da pessoa {}° (em kg): '.format(c)))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print('O resultado: Maior peso lido foi: {:.2f}kg'.format(maior_peso))
print('O Menor peso lido: {:.2f}kg'.format(menor_peso))
