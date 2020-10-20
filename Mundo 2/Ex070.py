'''
Aula 15: interrompendo repetições while.

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
- qual é o total gasto na compra
- quantos produtos custam mais de R$ 1000
- qual é o nome do produto mais barato
'''

print('{:-^40}'.format('   LOJA SUPER BARATÃO   '))
totalCompra = qtdeProdutos = maisBarato = cont = 0
nomeBarato = ''
while True:
    nomeProduto = str(input('\nNome do Produto: ')).strip()
    precoProduto = float(input('Preço: R$ '))
    cont += 1
    totalCompra += precoProduto
    if precoProduto > 1000:
        qtdeProdutos += 1
    if cont == 1 or precoProduto < maisBarato:
        maisBarato = precoProduto
        nomeBarato = nomeProduto            
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('{:-^30}'.format('   FIM DO PROGRAMA   '))
print(f'O total da compra foi R$ {totalCompra:.2f}')
print(f'Temos {qtdeProdutos} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R$ {maisBarato}')
