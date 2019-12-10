from random import randint
computador = randint (0, 5)
print ('-=-' * 10)
print ('Vou pensar em um número de 0 a 5, descubra qual é...')
print ('-=-' * 10)
jogador = int (input('Diga o valor que pensei: '))
if jogador == computador:
	print ('Parabéns, eu pensei no número {}'.format (computador))
else:
	print ('Que pena você errou, eu pensei no número {} '.format (computador))
