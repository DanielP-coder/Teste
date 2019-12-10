import random
n1 = str (input("O nome do Aluno: "))
n2 = str (input("Digite o segundo nome: "))
n3 = str (input("Digite o terceiro nome: "))
n4 = str (input("Digite um último nome: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print ("A ordem de apresentação é ")
print (lista)