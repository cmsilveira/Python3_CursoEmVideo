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
    escolhaComputador = randint(0,11)
    valor = int(input('Diga um valor: [0 a 10] '))
    total = valor + escolhaComputador
    selecao = ' '
    while selecao not in 'PI':
        selecao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {valor} e o computador {escolhaComputador}.\nTotal de {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if selecao == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif selecao == 'I':
        if total % 2 != 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
