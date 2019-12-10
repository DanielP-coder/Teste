import math
angulo = float (input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
print ("O ângulo de {}, tem o seno {:.2f}".format(angulo, seno))