'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.
'''

from random import randint

for c in range(0,5):
    valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = valores[0]
print(f'Os valores sorteados foram ', end=' ')
for c in valores:
    print(f'{c}', end=' ')
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
