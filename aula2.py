print('***************')
print('Bem vindo ão jogo')
print('***************')

numero_secreto = 42

chute = input('Digite o seu número: ')

if (int(chute) == numero_secreto):
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ ERRO!')