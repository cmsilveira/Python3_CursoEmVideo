'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem da colocação. Depois mostre:
- Apenas os 5 primeiros colocados
- Os últimos 4 colocados da tabela
- Uma lista com os times em ordem alfabética.
- Em que posição na tabela está o time da Chapecoense
'''

tabela = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Santos', 'Fluminense', 'Fortaleza',
          'Palmeiras', 'Atlético-GO', 'Grêmio', 'Sport', 'Bahia', 'Ceará', 'Botafogo', 'Vasco', 'Corinthians',
          'Atletico-PR', 'Coritiba', 'Bragantino', 'Goiás')
print('-' * 30)
print(f'Lista de times do Brasileirão: {tabela}')
print('-' * 30)
print(f'Os 5 primeiros são {tabela[:5]}')
print('-' * 30)
print(f'Os 4 útimos são {tabela[16:20]}')
print('-' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-' * 30)
nome = 'Santos'
for c in range(0, len(tabela)):
    if nome == c:
        print(f'O Santos está na {tabela[]}ª posição.')
