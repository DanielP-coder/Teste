velocidade = float (input("Qual a velocidade atual do carro: "))
if velocidade > 80:
	print ("Você exedeu a velocidade máxima de 80km/h ")
	multa = (velocidade-80)*7
	print ("O valor da multa é R${:.2f}!".format(multa))
print ("Tenha um bom dia")