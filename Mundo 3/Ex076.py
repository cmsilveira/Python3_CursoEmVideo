'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.90, 'Mochila', 120.32,
            'Canetas', 22.30, 'Livro', 34.90)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R$ {produtos[c]:>6.2f}')
print('-'*30)
