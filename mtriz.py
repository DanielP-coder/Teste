num = list (range(10))

for n in range (0,10):
	num [n] = int (input("Digite um valor "))
	
for i in range (0,10):
	for j in range (0,1):
		if (num[i] < num [j]):
			aux = num [i]
			num [i] = num [j]
			num [j] = aux
			
for n in range (0,10):
	print (num)
			