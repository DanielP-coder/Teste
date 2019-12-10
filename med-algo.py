num = int (input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ("Analisando o número... {}".format(num))
print ("O valor da unidade é {}".format(u))
print ("O valor da dezena é {}".format(d))
print ("O valor da centena é {}".format(c))
print ("O valor da unidade de milhar é {}".format(m))