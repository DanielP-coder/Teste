salario = float (input("Digite o salário: R$"))
taxa = float (input("O valor do aumento %"))
novo = salario + (salario * taxa / 100)
print ("O novo valor do salário é R${:.2f}".format(novo))