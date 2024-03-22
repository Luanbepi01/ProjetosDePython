altu = float(input('Digite sua altura: '))
pes1 = float(input('Digite seu peso: '))
imc = pes1 / (altu ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}, Abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f}, Peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print ('Seu IMC é {:.1f}, Sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}, Obesidade grau II.'.format(imc))
else:
    print('Seu IMC é {:.1f}, Obesidade mórbida.'.format(imc))