num = soma = cont = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += num
    if num == 999:
        cont -= 1
        soma -= num
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
