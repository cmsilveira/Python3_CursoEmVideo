'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posicao {c}: ')))
print('-' * 40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ')
print(f'O menor valor digitado foi {min(valores)}')
