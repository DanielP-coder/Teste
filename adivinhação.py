import random 
sorteia = random.randint(0,10)

num = int (input ("Advinhe o número: "))
while sorteia != num:
	if sorteia < num: 
		num = int (input ("Digite um valor menor "))
	else: 
		num = int (input ("Digite um valor maior "))
print (" O número digitado foi ", num)