import random
n1 = str (input("O nome do Aluno: "))
n2 = str (input("Digite o segundo nome: "))
n3 = str (input("Digite o terceiro nome: "))
n4 = str (input("Digite um último nome: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print ("O azarado que irá limpar o quadro é {}".format(escolhido))