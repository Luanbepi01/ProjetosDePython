# Variaveis fundamentais
val_casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o Salário do comprador: R$'))
anos = int(input('Em quantos anos será o pagamento: '))
prestacao = val_casa / (anos * 12)
minimo = sal * 30 / 100
print('Para pagar uma cada de R${:.2f} em {} anos'.format(val_casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')


