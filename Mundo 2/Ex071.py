'''
Aula 15: interrompendo repetições while.

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: considere que o caixa possui cédulas de 50, 20, 10 e 1.
'''

print('-'*27)
print('{:^27}'.format('BANCO CEV'))
print('-'*27)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedulas = 50
totalCedulas = 0
while True:
    if totalCedulas >= cedulas:
        totalCedulas -= cedulas
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R$ {cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalCedulas = 0
        if totalCedulas == 0:
            break
print('-'*30)
print('Volte sempre ao BANCO CEF.')
