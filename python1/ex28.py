from random import choice
list = (0,1,2,3,4,5)
r = int (input('Digite um número de 0 a 5:'))
if r == (f'{choice(list)}'):
    print ('Parabéns, você acertou!')
else:
    print ('Tente novamente! O número escolhido foi',f'{choice(list)}','e não',r,'.')

#Outra forma de fazer:

from random import randint
jogador = int (input('Digite um número de 0 a 5:'))
if jogador == randint(0,5):
    print ('Parábens, você acertou!')
else:
    print ('Tente novamente! O número escolhido foi', randint(0,5),'e não',jogador,'.')