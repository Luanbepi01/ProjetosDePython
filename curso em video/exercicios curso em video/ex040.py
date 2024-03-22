nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media < 5.0:
    print('sua nota é {}, você está  Reprovado!'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua nota é {}, você está de Recuperação!'.format(media))
else:
    print('Sua nota é {}, você está de Aprovado!'.format(media))