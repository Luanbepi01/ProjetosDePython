primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos da PA são: ')
for c in range(10):
    termo = primeiro_termo + c * razao
    print('Termo {}: {}'.format(c + 1, termo))