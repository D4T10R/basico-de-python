import forca
import aula8

print('******************************')
print("Escolha o seu jogo: ")
print('******************************')

print('Forca (1) \nAdivinhação (2)')

escolha = int(input('Qual jogo: '))

if escolha == 1:
    print('JOGO DA FORCA \n')
    forca.jogar()
elif escolha == 2:
    print('JOGO DA ADIVINHAÇÃO\n ')
    aula8.jogar()