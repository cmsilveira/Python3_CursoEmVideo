'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
- quantas vezes apareceu o valor 9
- em que posição foi digitado o primeiro valor 3
- quais foram os números pares
'''

cont = posicao = qtdTres = 0
numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posicao.')
print(f'Os valores pares digitados foram ', end='')
for c in numero:
    if c % 2 == 0:
        print(c, end=' ')
