import random
nome01 = str(input("Primeiro aluno: "))
nome02 = str(input("Segundo aluno: "))
nome03 = str(input("Terceiro aluno: "))
nome04 = str(input("Quarto aluno: "))
lista = [nome01, nome02, nome03, nome04]
random.shuffle(lista)
print("A ordem de apresentação será\n", lista)
