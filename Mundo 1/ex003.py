num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2
#print('A soma entre', num1, 'e', num2, 'vale', soma)
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}.'.format(s, m, d), end=' ')
print('Divisão inteira é {} e potência é {}'.format(di, e))