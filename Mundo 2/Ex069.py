'''
Aula 15: interrompendo repetições while.

Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar.
No final, mostre:
- quantas pessoas tem mais de 18 anos
- quantos homens foram cadastrados
- quantas mulheres tem menos de 20 anos.
'''

totalDezoitoAnos = totalHomens = totalMulheres = 0
print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        totalDezoitoAnos += 1
    if sexo == 'M':
        totalHomens += 1
    if idade < 20 and sexo == 'F':
        totalMulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('------ FIM DO PROGRAMA ------')
print(f'Total de pessoas com mais de 18 anos: {totalDezoitoAnos}')
print(f'Ao todo temos {totalHomens} cadastrados.')
print(f'E temos {totalMulheres} mulheres com menos de 20 anos.')
