print('='*100)
print('PROGRAMA QUE LER O IMC DE UMA PESSOA'.center(100))
print('='*100)

abaixo_peso = 0
peso_normal = 0
acima_do_peso = 0
obesidade_grau_I = 0
obesidade_grau_II = 0
obesidade_grau_III = 0

opcao = 'S'

while True:
    altura = float(input('Digite a sua Altura: '))
    peso = float(input('Digite o seu peso: '))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print('='*50)
        print(f'Essa pessoa tem {imc:.1f} de imc e está abaixo do peso.')
        print('='*50)
        abaixo_peso += 1
    elif imc >= 18.5 and imc < 25:
        print('='*50)
        print(f'Essa pessoa tem {imc:.1f} de imc e está com peso normal.')
        print('='*50)
        peso_normal += 1
    elif imc >= 25 and imc < 30:
        print('='*50)
        print(f'Essa pessoa tem {imc:.1f} de imc e está acima do peso normal.')
        print('='*50)
        acima_do_peso += 1
    elif imc >= 30 and imc < 35:
        print('='*50)
        print(f'Essa pessoa tem {imc:.1f} de imc e está com obesidade grau I.')
        print('='*50)
        obesidade_grau_I += 1
    elif imc >= 35 and imc < 40:
        print('='*50)
        print(f'Essa pessoa tem {imc:.1f} de IMC e está com obesidade grau II.')
        print('='*50)
        obesidade_grau_II += 1
    else:
        print('='*50)
        print(f'Essa pessoa tem {imc:.1f} de IMC e está com obesidade grau III.')
        print('='*50)
        obesidade_grau_III += 1
    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
if abaixo_peso > 0:
    print(f'tiveram {abaixo_peso} pessoas abaixo do peso.')
if peso_normal > 0:
    print(f'Tiveram {peso_normal} pessoas com o peso normal.')
if acima_do_peso > 0:
    print(f'Tiveram {acima_do_peso} pessoas acima do peso.')
if obesidade_grau_I > 0:
    print(f'Tiveram {obesidade_grau_I} pessoas com obesidade grau I.')
if obesidade_grau_II > 0:
    print(f'Tiveram {obesidade_grau_II} pessoas com obesidade grau II.')
if obesidade_grau_III > 0:
    print(f'Tiveram {obesidade_grau_III} pessoas com obesidade grau III.')
print('='*100)
print('FIM DO PROGRAMA!'.center(100))
print('='*100)






