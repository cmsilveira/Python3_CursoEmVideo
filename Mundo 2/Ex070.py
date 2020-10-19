'''
Aula 15: interrompendo repetições while.

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
- qual é o total gasto na compra
- quantos produtos custam mais de R$ 1000
- qual é o nome do produto mais barato
'''

print('-'*36)
print('         LOJA SUPER BARATÃO')
print('-'*36)
continuar = 'S'
totalCompra = qtdeProdutos = 0
maisBarato = 99999
while True:
    nomeProduto = str(input('\nNome do Produto: ')).strip()
    precoProduto = float(input('Preço: R$ '))
    totalCompra += precoProduto
    if precoProduto > 1000:
        qtdeProdutos += 1
    if precoProduto < maisBarato:
        maisBarato = precoProduto
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        print('---------- FIM DO PROGRAMA ----------')
        print(f'O total da compra foi R$ {totalCompra}')
        print(f'Temos {qtdeProdutos} produtos custando mais de R$ 1000.00')
        print(f'O produto mais barato foi {nomeProduto} que custa R$ {maisBarato}')
        break
