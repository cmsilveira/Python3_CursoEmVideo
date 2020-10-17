velocidade = float(input('Qual a velocidade do carro?: '))
if velocidade > 80:
    print(f'Você foi multado!\nSua velocidade é {velocidade} Km/h'
          f' e sua multa será de R$ {(velocidade - 80) * 7.0:.2f}')
else:
    print(f'Sua velocidade é {velocidade} Km/h. Está dentro do limite!')
