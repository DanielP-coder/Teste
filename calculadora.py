n1 = int (input("digite o primeiro valor "))
n2 = int (input("digite o segundo valor "))
print ("escolha a operação")
print ("1 para soma ")
print ("2 para subtração ")
print ("3 para multiplacação ")
op = int (input("4 para divisão "))

if (op == 1) :
	print (n1+n2)
if (op == 2) :
	print (n1-n2)
if (op == 3) :
	print (n1*n2)
if (op == 4) :
	print (n1/n2)