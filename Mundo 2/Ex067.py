'''
Aula 15: interrompendo repetições while.

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    else:
        print('-'*30)
        for c in range(1, 11):
            print(f'{valor} x {c} = {valor * c}')
        print('-'*30)
