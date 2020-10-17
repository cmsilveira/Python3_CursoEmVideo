dolar = float(input('Qual o valor do dolar hoje?: R$' ))
real = float(input('Quanto você tem na carteira?: R$' ))
print('Com o dólar a {:.2f}, você pode comprar {:.2f} dólares com seus {:.2f} reais.'.format(dolar, real/dolar, real))