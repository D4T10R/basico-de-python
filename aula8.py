import random
def jogar(): 
    print('***************')
    print('Bem vindo ão jogo')
    print('***************')

    numero_secreto = random.randrange(0, 101)
    rodadas = 0
    tentativas = 1
    pontos = 100

    print("Nivel fácil - 1")
    print("Nivel médio - 2")
    print("Nivel difícil - 3")

    nivel = int(input("Qual nível você deseja jogar? "))

    if (nivel == 1):
        rodadas = 20
    elif (nivel == 2):
        rodadas = 10
    else:
        rodadas = 5

    for tentativas in range(1, rodadas+1):
        print(f"\nTentativa: {tentativas} de {rodadas} ")
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
                print('VOCÊ ERRO!, o número secreto é MENOR que o número secreto')
            elif (menor):
                print('VOCÊ ERRO!, o número secreto é MAIOR que o número secreto')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    print(f'O número secreto era: {numero_secreto} \nvocê fez: {pontos} pontos')

if (__name__ == "__main__"):
    jogar()