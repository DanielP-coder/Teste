nota1= float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
media = (nota1+nota2)/2
if (media < 6):
	print ("Você tirou {} e está de recuperação".format(media))
if (media < 3):
	print ("Você tirou {} e está reprovado".format(media))
if (media >= 6):
	print ("Você tirou {}, meu parabéns".format(media))