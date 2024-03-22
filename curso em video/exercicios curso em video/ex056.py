'''# Programa que leia nome, idade e sexo de 4 pessoas.

nomes = []
idades = []
sexos = []

for c in range(1, 5):
    print('-=' * 46)
    print('Digite as informações da pessoa {}:'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper()
    print('-=' * 46)
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

print('Resultados:')
for c in range(4):
    print('-=' * 46)
    print('Pessoa {}:'.format(c + 1))
    print('Nome: {}'.format(nomes[c]))
    print('Idade: {} anos'.format(idades[c]))
    print('Sexo: {}'.format(sexos[c]))
    print('-=' * 46)
media_idade = sum(idades) / len(idades)
print('-=' * 46)
print('Média de idade: {:.2f} anos'.format(media_idade))
print('-=' * 46)
contagem_feminino = sexos.count('F')
print('Quantidade de pessoas do sexo feminino: {}'.format(contagem_feminino))
print('-=' * 46)
maiores_idade = sum(1 for idade in idades if idade >= 18)
print('Quantidade de pessoas maiores de idade: {}'.format(maiores_idade))
print('-=' * 46)'''


#Correção do exercicio 56:

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {}º PESSOA _______'.format(p))
    nome = str(input('Nome: ')).strip()
    idade =  int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
