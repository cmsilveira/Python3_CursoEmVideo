'''
Aula 15: interrompendo repetições while.

Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

print('='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*30)
vitorias = 0
while True:
    escolhaComputador = randint(0,9)
    valor = int(input('Diga um valor: [0 a 9] '))
    selecao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    total = valor + escolhaComputador
    if (total % 2 == 0 and selecao == 'P'):
        print('-'*30)
        print(f'Você jogou {valor} e o computador {escolhaComputador}.\nTotal de {total}. DEU PAR.')
        print('-'*30)
        print('Você VENCEU!\nVamos jogar novamente...')
        vitorias += 1
        print('='*30)
    elif (total % 2 != 0 and selecao == 'I'):
        print('-'*30)
        print(f'Você jogou {valor} e o computador {escolhaComputador}.\nTotal de {total}. DEU ÍMPAR.')
        print('-'*30)
        print('Você VENCEU!\nVamos jogar novamente...')
        vitorias += 1
        print('='*30)
    elif (total % 2 == 0 and selecao == 'I'):
        print('-'*30)
        print(f'Você jogou {valor} e o computador {escolhaComputador}.\nTotal de {total}. DEU PAR.')
        print('-'*30)
        print(f'Você PERDEU!\nGAME OVER! Você venceu {vitorias} vezes.')
        print('='*30)
        break
    elif (total % 2 != 0 and selecao == 'P'):
        print('-'*30)
        print(f'Você jogou {valor} e o computador {escolhaComputador}.\nTotal de {total}. DEU ÍMPAR.')
        print('-'*30)
        print(f'Você PERDEU!\nGAME OVER! Você venceu {vitorias} vezes.')
        print('='*30)
        break
