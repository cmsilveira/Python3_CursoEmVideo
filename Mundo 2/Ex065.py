opcao = 'S'
cont = soma = media = maior = menor = 0
while opcao != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = int(num)
        if num < maior:
            menor = int(num)
    opcao = str(input('Quer continuar? [S/N]: ')).upper()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
