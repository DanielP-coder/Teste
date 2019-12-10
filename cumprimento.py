nome = str (input("Diga seu nome: "))
gen = str (input("Seu sexo: "))

if (gen == m):
	print ("Olá sr. {}".format(nome))
	if (gen == M):
		print ("Olá Sr.{}".format(nome))
	
if (gen == f):
	print ("Olá sra.{}".format(nome))
	if (gen == F):
		print ("Olá Sra.{}".format(nome))
else:
	print ("Você digitou um sexo inexistente. ")
