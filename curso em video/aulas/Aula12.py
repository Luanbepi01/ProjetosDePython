nome = str(input('Qual seu nome? '))
if nome == 'Luan':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))