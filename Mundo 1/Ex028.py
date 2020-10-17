import random

numero = random.randint(0, 5)
valor = int(input('Pensei em um número.\nDigite um valor entre 0 e 5: '))
if valor == numero:
    print(f'Parabéns, você ganhou! Pensei no número {numero}.')
else:
    print(f'Que pena, você perdeu! Pensei no número {numero}.')
