'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista na lista, não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente.
'''

valores = []
opcao = ' ' 
while opcao not in 'nN':
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existe na lista. Não será adicionado!')            
    opcao = str(input('Deseja continuar? [S/N]').strip().upper())
print('-' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
