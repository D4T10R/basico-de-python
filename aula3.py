print('***************')
print('Bem vindo ão jogo')
print('***************')

numero_secreto = 42
total_tentativas = 3



while (total_tentativas > 0):
    chute = int(input('Digite o seu número: '))
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    print("\nTentativa: ", total_tentativas)
    if (acertou):
        print('VOCÊ VENCEU!')
    else:
        if (maior):
            print('VOCÊ ERRO!, o número digitado é MAIOR que o número secreto')
        elif (menor):
            print('VOCÊ ERRO!, o número digitado é MENOR que o número secreto')
    total_tentativas -= 1