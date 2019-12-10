real = float (input("Valor: R$ "))
preco = float (input ("Qual o preço do dolar? R$"))
dolar = real / preco
print ("Com R${:.2f}, você pode comprar US${:.2f}".format(real, dolar))