largura = float(input("Largura: "))
altura = float(input('Altura: '))
area = largura*altura
print('Área: {:.3f} m².\nVai precisar de {:.4f} litros para pintar.'.format(area, area/2))