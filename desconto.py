preco = float (input("Qual  o valor do produto: R$"))
desc = float (input("Desconto: "))
np = preco - (preco * desc/100)
print ("Um produto que custa R${} , com o desconto de {}%, agora custa R${:.2f}".format(preco, desc, np))