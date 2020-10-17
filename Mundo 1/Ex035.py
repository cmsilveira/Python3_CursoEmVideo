AB = float(input('Primeiro segmento: '))
CD = float(input('Segundo segmento: '))
EF = float(input('Terceiro segmento: '))
if (AB + CD > EF and AB + EF > CD and EF + CD > AB):
    print('Sim, pode formar um triângulo!')
else:
    print('Não, não pode formar um triângulo!')
