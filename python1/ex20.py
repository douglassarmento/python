# Coloca a ordem dos nomes

from random import shuffle
a = str (input ('Digite um nome:'))
b = str (input ('Digite um nome:'))
c = str (input ('Digite um nome:'))
list = (a, b, c)
print ('A ordem dos nomes ficou {}.'.format (shuffle (list)))