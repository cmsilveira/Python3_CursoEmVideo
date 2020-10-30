'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''

valores = list()
v = int(input('Digite um valor: '))
valores.append(v)
print('Adicionado ao final da fila.')
for count in range(0,4):
    v = int(input('Digite um valor: '))
    for posicao in valores:
        if v > valores[posicao]:
            valores.append(v)
            print('Adicionado ao final da lista.')
        elif v < valores[posicao] or v == valores[posicao]:
            valores.insert(posicao, v)
            print(f'Adicionado na posição {posicao} da lista.')    
print('-' * 30)
print(f'Os valores digitados em ordem foram {valores}')
