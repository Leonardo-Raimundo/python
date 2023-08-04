from random import shuffle

nome1 = input('Nome 1: ')
nome2 = input('Nome 2: ')
nome3 = input('Nome 3: ')
nome4 = input('Nome 4: ')

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print(lista)