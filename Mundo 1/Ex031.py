distancia = float(input('Digite a distância da viagem: '))
if distancia <= 200:
    print(f'Sua viagem de {distancia} Km custará R$ {distancia * 0.50:.2f}.')
else:
    print(f'Sua viagem de {distancia} Km custará R$ {distancia * 0.45:.2f}.')
