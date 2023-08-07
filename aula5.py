print('***************')
print('Bem vindo ão jogo')
print('***************')

numero_secreto = 42
rodada = 3
tentativa = 1


for tentativa in range(1, rodada+1):
    print(f"\nTentativa: {tentativa} de 3 ")
    chute = int(input('Digite o seu número: '))

    if (chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print('VOCÊ VENCEU!')
        break
    else:
        if (maior):
            print('VOCÊ ERRO!, o número digitado é MAIOR que o número secreto')
        elif (menor):
            print('VOCÊ ERRO!, o número digitado é MENOR que o número secreto')
